from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from .models import Note
from .forms import NoteForm

# Форма создания записи
def note_create(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():  # Валидация данных
            form.save()
            return redirect('notes_list')  # Редирект после сохранения
    else:
        form = NoteForm()
    return render(request, 'notes/form.html', {'form': form, 'title': 'Создать заметку'})


def note_edit(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    if request.method == 'POST':
        # Связываем форму с объектом
        form = NoteForm(request.POST, instance=note)  # instance=note - форма заполняется текущими данными
        if form.is_valid():  # self.is_bound and not self.errors
            form.save()  # UPDATE в БД по note.id
            return redirect('note_detail', note_id=note.id)
    else:
        # Для GET-запроса форма заполняется текущими значениями note
        form = NoteForm(instance=note)
    return render(request, 'notes/form.html', {'form': form, 'title': 'Редактирование записи'})
        


# Список всех заметок
def notes_list(request):
    notes = Note.objects.all()
    return render(request, 'notes/index.html', {'notes': notes})  # render возвращает HTML-шаблон с данными

    # html = '<h1>Список заметок</h1>'
    # for note in notes:
    #     html += f"<p><a href='/notes/{note.id}'>{note.title}</a></p>"
    # return HttpResponse(html)


# Детальная страница одной заметки
def note_detail(request, note_id):
    note = get_object_or_404(Note, pk=note_id)  # получаем заметку по ID или возвращаем 404 (аналог Model.objects.get(...), но с обработкой ошибок)
    return render(request, 'notes/detail.html', {'note': note})  # render возвращает HTML-шаблон с данными

    # return HttpResponse(f"<h1>{note.title}</h1><p>{note.body}</p>")  # Возвращаем обычный HTML как текст
