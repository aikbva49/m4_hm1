from django.shortcuts import render, get_object_or_404
from . import models
from django.core.paginator import Paginator
from django.views import generic


class HorseTourListView(generic.ListView):
    template_name = 'horse_tour/tour_list.html'
    model = models.TourCompany
    paginate_by = 2

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')
            
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tours'] = context['page_obj']
        return context


# def horse_tour_list_view(request):
#     query = request.GET.get('q')
#     if query:
#         tours_all = models.TourCompany.objects.filter(services__name__icontains=query).distinct().order_by('-id')
#     else:
#         tours_all = models.TourCompany.objects.all().order_by('-id')
# 
#     paginator = Paginator(tours_all, 2)
#     page_number = request.GET.get('page')
#     tours = paginator.get_page(page_number)
#     return render(request, 'horse_tour/tour_list.html', {'tours': tours})





class HorseTourSimpleListView(generic.ListView):
    template_name = 'horse_tour/tour_list.html'
    model = models.TourCompany
    paginate_by = 2

    def get_queryset(self):
        return self.model.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tours'] = context['page_obj']
        return context


# def horse_tour_list(request):
#     tours_all = models.TourCompany.objects.all()
#     paginator = Paginator(tours_all, 2) 
#     page_number = request.GET.get('page')
#     tours = paginator.get_page(page_number)
#     return render(request, 'horse_tour/tour_list.html', {'tours': tours})





class TourView(generic.ListView):
    template_name = 'tours.html'
    model = models.TourCompany
    context_object_name = 'companies'

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tourists'] = models.Tourist.objects.all()
        return context


# def tour_view(request):
#     companies = models.TourCompany.objects.all().order_by('-id')
#     tourists = models.Tourist.objects.all() 
#     return render(request, 'tours.html', {
#         'companies': companies,
#         'tourists': tourists
#     })





class CreateReviewView(generic.TemplateView):
    template_name = 'create_review.html'

    def get(self, request, **kwargs):
        company_id = request.GET.get('company')
        tourist_id = request.GET.get('tourist')
        text = request.GET.get('text')
        marks = request.GET.get('marks')
        
        models.ReviewTour.objects.create(
            choice_company_id=company_id, 
            tourist_id=tourist_id,
            text=text,
            marks=int(marks)
        )
        return super().get(request, **kwargs)


# def create_review_view(request):
#     if request.method == 'GET':
#         company_id = request.GET.get('company')
#         tourist_id = request.GET.get('tourist')
#         text = request.GET.get('text')
#         marks = request.GET.get('marks')
# 
#         if company_id and tourist_id and marks:
#             models.ReviewTour.objects.create(
#                 choice_company_id=company_id, 
#                 tourist_id=tourist_id,
#                 text=text,
#                 marks=int(marks)
#             )
#     return render(request, 'create_review.html')
