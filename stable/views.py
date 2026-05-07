from django.shortcuts import render, redirect, get_object_or_404
from .models import Horse
from .forms import HorseForm

def horse_list(request):
    horses = Horse.objects.all()
    return render(request, 'stable/stable_list.html', {'horses': horses})

def horse_add(request):
    if request.method == 'POST':
        form = HorseForm(request.POST, request.FILES) 
        if form.is_valid():
            form.save()
            return redirect('horse_list')
    else:
        form = HorseForm()
    return render(request, 'stable/stable_form.html', {'form': form})

def horse_edit(request, pk):
    horse = get_object_or_404(Horse, pk=pk)
    if request.method == 'POST':
        form = HorseForm(request.POST, request.FILES, instance=horse)
        if form.is_valid():
            form.save()
            return redirect('horse_list')
    else:
        form = HorseForm(instance=horse)
    return render(request, 'stable/stable_form.html', {'form': form})

def horse_delete(request, pk):
    horse = get_object_or_404(Horse, pk=pk)
    if request.method == 'POST':
        horse.delete()
        return redirect('horse_list')
    return render(request, 'stable_confirm_delete.html', {'horse': horse})