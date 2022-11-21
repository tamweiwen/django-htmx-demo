import json

from django.shortcuts import render
from django.http import HttpResponse
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

    return render(request, "main/add_note.html", {'form': form})
