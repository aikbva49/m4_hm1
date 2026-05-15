from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . import models

def book_detail(request, id):
    book = get_object_or_404(models.Book, id=id)
    book.views_count += 1 
    book.save()
    return render(request, 'book_detail.html', {'book': book})

def book_list(request):
    query = request.GET.get('q')
    if query:
        books = models.Book.objects.filter(title__icontains=query)
    else:
        books = models.Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

def book_detail_view(request, id):
    if request.method == 'GET':
        book_id = get_object_or_404(models.Books, id=id) 
        return render(request, 'book_detail.html', {'book_id': book_id})

def book_list_view(request):
    if request.method == 'GET':
        query_books = models.Books.objects.all().order_by('-id')
        return render(request, 'book_list.html', {'books': query_books})
    


def qs1(request):
    return HttpResponse("«Боль неизбежна. Страдание – личный выбор каждого». -Харуки Мураками")

def qs2(request):
    return HttpResponse("«Когда счастье есть, о нем не думают» -Чынгыз Айтматов")

def qs3(request):
    return HttpResponse("«Смысл жизни в том, что она имеет свой конец.»-Франц Кафка")
