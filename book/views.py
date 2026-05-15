from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . import models
from django.core.paginator import Paginator

def book_list_view(request):
    query = request.GET.get('q')
    if query:
        books_all = models.Book.objects.filter(title__icontains=query).order_by('-id')
    else:
        books_all = models.Book.objects.all().order_by('-id')

    paginator = Paginator(books_all, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'book_list.html', {'books': page_obj})

def book_detail_view(request, id):
    book = get_object_or_404(models.Book, id=id)
    book.views_count += 1
    book.save()
    return render(request, 'book_detail.html', {'book': book})

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
    return render(request, 'book/book_list.html', {'books': page_obj})
    

def qs1(request):
    return HttpResponse("«Боль неизбежна. Страдание – личный выбор каждого». -Харуки Мураками")

def qs2(request):
    return HttpResponse("«Когда счастье есть, о нем не думают» -Чынгыз Айтматов")

def qs3(request):
    return HttpResponse("«Смысл жизни в том, что она имеет свой конец.»-Франц Кафка")
