# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Entry
from .forms import EntryForm

'''def centre(request):
    entries = Entry.objects.all()
    return render(request, 'anfix.html', {'entries': entries})'''


def centre(request):
    entries = Entry.objects.all()
    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('centre')
    else:
        form = EntryForm()
    return render(request, 'account.html', {'form': form,'entries': entries})

def anfi(request):
    entries = Entry.objects.all()
    return render(request, 'anfixall.html', {'entries': entries})


def enter(request):
    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('centre')
    else:
        form = EntryForm()
    return render(request, 'enter.html', {'form': form})

def edit(request, pk):
    entry = get_object_or_404(Entry, pk=pk)
    if request.method == 'POST':
        form = EntryForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            return redirect('centre')
    else:
        form = EntryForm(instance=entry)# экземпляр=запись
    return render(request, 'edit.html', {'form': form})

def delete(request, pk):
    entry = get_object_or_404(Entry, pk=pk)
    if request.method == 'POST':
        entry.delete()
        return redirect('centre')
    return render(request, 'delete.html', {'entry': entry})