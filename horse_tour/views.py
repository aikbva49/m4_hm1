from django.shortcuts import render, redirect
from . import models

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
                choice_company_id=company_id, # Исправлено имя поля
                tourist_id=tourist_id,
                text=text,
                marks=int(marks)
            )
    return redirect('tour_list')