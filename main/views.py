import json

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.decorators.http import require_POST

from .forms import NotesForm
from .models import Note

# Create your views here.


def index(request):
    return render(request, 'main/index.html')


def notes_list(request):
    return render(request, 'main/notes_list.html', {'notes': Note.objects.all()})


def add_note(request):
    if request.method == "POST":
        form = NotesForm(request.POST)
        if form.is_valid():
            note = form.save()
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "movieListChanged": None,
                        "showMessage": f"{note.name} added."
                    })
                })
            # return redirect(index)
    else:
        form = NotesForm()

    return render(request, "main/note_form.html", {'form': form})


def edit_note(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        form = NotesForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "movieListChanged": None,
                        "showMessage": f"{note.name} updated."
                    })
                }
            )
    else:
        form = NotesForm(instance=note)
    return render(request, "main/note_form.html", {
        'form': form,
        'note': note,
    })


@require_POST
def remove_note(request, pk):
    note = get_object_or_404(Note, pk=pk)
    note.delete()
    return HttpResponse(
        status=204,
        headers={
            'HX-Trigger': json.dumps({
                "movieListChanged": None,
                "showMessage": f"{note.name} deleted."
            })
        }
    )


def view_note(request, pk):
    note = get_object_or_404(Note, pk=pk)
    form = NotesForm(instance=note)

    return render(request, 'main/view_note.html', {'note': note, 'form': form})
