from django.shortcuts import render, get_object_or_404, redirect
from .models import HorseTour
from .forms import TourForm

# Список туров (Read)
def tour_list(request):
    tours = HorseTour.objects.all()
    # Исправил путь на stable/, так как папка называется так
    return render(request, 'stable/tour_list.html', {'tours': tours})

# Создание тура (Create)
def tour_create(request):
    if request.method == "POST":
        form = TourForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('tour_list')
    else:
        form = TourForm()
    return render(request, 'stable/tour_form.html', {'form': form, 'title': 'Добавить тур'})

# Редактирование (Update)
def tour_update(request, id):
    tour = get_object_or_404(HorseTour, id=id)
    if request.method == "POST":
        form = TourForm(request.POST, request.FILES, instance=tour)
        if form.is_valid():
            form.save()
            return redirect('tour_list')
    else:
        form = TourForm(instance=tour)
    return render(request, 'stable/tour_form.html', {'form': form, 'title': 'Редактировать'})

# Удаление (Delete)
def tour_delete(request, id):
    tour = get_object_or_404(HorseTour, id=id)
    if request.method == "POST":
        tour.delete()
        return redirect('tour_list')
    return render(request, 'stable/tour_confirm_delete.html', {'tour': tour})