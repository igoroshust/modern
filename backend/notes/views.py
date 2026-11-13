from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Note

# Список всех заметок
def notes_list(request):
    notes = Note.objects.all()
    html = '<h1>Список заметок</h1>'
    for note in notes:
        html += f"<p><a href='/notes/{note.id}'>{note.title}</a></p>"
    return HttpResponse(html)


# Детальная страница одной заметки
def note_detail(request, note_id):
    note = get_object_or_404(Note, pk=note_id)  # получаем заметку по ID или возвращаем 404 (аналог Model.objects.get(...), но с обработкой ошибок)
    print(note)
    return HttpResponse(f"<h1>{note.title}</h1><p>{note.body}</p>")  # Возвращаем обычный HTML как текст
