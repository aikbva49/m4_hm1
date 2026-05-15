from django.shortcuts import render, redirect
from . import models
from django.core.paginator import Paginator

def horse_tour_list(request):
    tours_all = models.TourCompany.objects.all()
    paginator = Paginator(tours_all, 2) 
    page_number = request.GET.get('page')
    tours = paginator.get_page(page_number)
    return render(request, 'horse_tour/tour_list.html', {'tours': tours})

def tour_view(request):
    companies = models.TourCompany.objects.all().order_by('-id')
    tourists = models.Tourist.objects.all() 
    return render(request, 'tours.html', {
        'companies': companies,
        'tourists': tourists
    })

def create_review_view(request):
    if request.method == 'GET':
        company_id = request.GET.get('company')
        tourist_id = request.GET.get('tourist')
        text = request.GET.get('text')
        marks = request.GET.get('marks')

        if company_id and tourist_id and marks:
            models.ReviewTour.objects.create(
                choice_company_id=company_id, 
                tourist_id=tourist_id,
                text=text,
                marks=int(marks)
            )
def horse_tour_list(request):
    query = request.GET.get('q')
    if query:
        # Ищем услуги по названию
        tours = models.TourCompany.objects.filter(services__name__icontains=query).distinct()
    else:
        tours = models.TourCompany.objects.all()


    return render(request, 'horse_tour/tour_list.html', {'tours': tours})
