from django.shortcuts import render, get_object_or_404, redirect
from .models import HorseTour
from .forms import TourForm
from django.views import generic
from django.urls import reverse


class TourListView(generic.ListView):
    template_name = 'stable/tour_list.html'
    context_object_name = 'tours'
    model = HorseTour

    def get_queryset(self):
        return self.model.objects.all()


# # Список туров (Read)
# def tour_list(request):
#     tours = HorseTour.objects.all()
#     return render(request, 'stable/tour_list.html', {'tours': tours})





class TourCreateView(generic.CreateView):
    template_name = 'stable/tour_form.html'
    form_class = TourForm

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(TourCreateView, self).form_valid(form=form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавить тур'
        return context

    def get_success_url(self):
        return reverse('tour_list')


# def tour_create(request):
#     if request.method == "POST":
#         form = TourForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('tour_list')
#     else:
#         form = TourForm()
#     return render(request, 'stable/tour_form.html', {'form': form, 'title': 'Добавить тур'})





class TourUpdateView(generic.UpdateView):
    template_name = 'stable/tour_form.html'
    form_class = TourForm
    model = HorseTour

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(TourUpdateView, self).form_valid(form=form)

    def get_object(self, **kwargs):
        tour_id = self.kwargs.get('id')
        return get_object_or_404(self.model, id=tour_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Редактировать'
        return context

    def get_success_url(self):
        return reverse('tour_list')


# def tour_update(request, id):
#     tour = get_object_or_404(HorseTour, id=id)
#     if request.method == "POST":
#         form = TourForm(request.POST, request.FILES, instance=tour)
#         if form.is_valid():
#             form.save()
#             return redirect('tour_list')
#     else:
#         form = TourForm(instance=tour)
#     return render(request, 'stable/tour_form.html', {'form': form, 'title': 'Редактировать'})





class TourDeleteView(generic.DeleteView):
    template_name = 'stable/tour_confirm_delete.html'
    model = HorseTour
    context_object_name = 'tour'

    def get_object(self, **kwargs):
        tour_id = self.kwargs.get('id')
        return get_object_or_404(self.model, id=tour_id)

    def get_success_url(self):
        return reverse('tour_list')


# def tour_delete(request, id):
#     tour = get_object_or_404(HorseTour, id=id)
#     if request.method == "POST":
#         tour.delete()
#         return redirect('tour_list')
#     return render(request, 'stable/tour_confirm_delete.html', {'tour': tour})