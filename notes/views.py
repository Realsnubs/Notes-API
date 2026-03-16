from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import viewsets
from .models import Note
from .serializers import NoteSerializer


def home(request):
    notes = Note.objects.all().order_by("-created_at")
    return render(request, "home.html", {"notes": notes})


def note_create(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")

        if title and content:
            Note.objects.create(title=title, content=content)

    return redirect("/")


def note_edit(request, note_id):
    note = get_object_or_404(Note, id=note_id)

    if request.method == "POST":
        note.title = request.POST.get("title")
        note.content = request.POST.get("content")
        note.save()
        return redirect("/")

    return render(request, "note_edit.html", {"note": note})


def note_delete(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    note.delete()
    return redirect("/")


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer