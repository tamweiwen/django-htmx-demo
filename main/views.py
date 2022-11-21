from django.shortcuts import render
from .forms import NotesForm
from .models import Note

# Create your views here.


def index(request):
    return render(request, 'main/index.html')


def notes_list(request):
    return render(request, 'notes_list.html', {'notes': Note.objects.all()})


def add_note(request):
    if request.method == "POST":
        form = NotesForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = NotesForm()

    return render(request, "main/add_note.html", {'form': form})
