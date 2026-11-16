

def note_create(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('notes_list')
    else:
        form = NoteForm()
    return render(request, 'notes/note_list.html', {'form': form, 'title': 'Создать запись'})

@require_http_methods(["GET", "POST"])
def note_delete(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    
    if request.method == 'POST':
        note.delete()
        return redirect('notes_list')
        
    return render(request, 'notes/confirm_delete', {'note': note })


def note_edit(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('note_detail', note_id=note.id)
    else:
        form = NoteForm(instance=note)
    return render(request, 'notes/note_detail.html', {'form': form, 'title': 'Редактирование записи'})