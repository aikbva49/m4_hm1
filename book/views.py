from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . import models
from django.core.paginator import Paginator
from django.views import generic


class BookListView(generic.ListView):
    template_name = 'book_list.html'
    model = models.Book
    paginate_by = 2

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return self.model.objects.filter(title__icontains=query).order_by('-id')
        else:
            return self.model.objects.all().order_by('-id')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = context['page_obj']
        return context


# def book_list_view(request):
#     query = request.GET.get('q')
#     if query:
#         books_all = models.Book.objects.filter(title__icontains=query).order_by('-id')
#     else:
#         books_all = models.Book.objects.all().order_by('-id')
#     
#     paginator = Paginator(books_all, 2)
#     page_number = request.GET.get('page')
#     books = paginator.get_page(page_number)
#     return render(request, 'book_list.html', {'books': books})





class BookDetailView(generic.DetailView):
    template_name = 'book_detail.html'
    context_object_name = 'book'
    pk_url_kwarg = 'id'
    model = models.Book

    def get_object(self, queryset = None):
        obj = super().get_object(queryset)
        obj.views_count += 1
        obj.save()
        return obj


# def book_detail_view(request, id):
#     book = get_object_or_404(models.Book, id=id)
#     book.views_count += 1
#     book.save()
#     return render(request, 'book_detail.html', {'book': book})





class BookDetailAltView(generic.DetailView):
    template_name = 'book_detail.html'
    context_object_name = 'book_id'
    pk_url_kwarg = 'id'
    model = models.Books

    def get_object(self, queryset = None):
        return get_object_or_404(self.model, id=self.kwargs.get('id'))


# def book_detail_view(request, id):
#     if request.method == 'GET':
#         book_id = get_object_or_404(models.Books, id=id) 
#         return render(request, 'book_detail.html', {'book_id': book_id})





class BookListSimpleView(generic.ListView):
    template_name = 'book_list.html'
    context_object_name = 'books'
    model = models.Book

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return self.model.objects.filter(title__icontains=query)
        else:
            return self.model.objects.all()


# def book_list(request):
#     query = request.GET.get('q')
#     if query:
#         books = models.Book.objects.filter(title__icontains=query)
#     else:
#         books = models.Book.objects.all()
#     return render(request, 'book_list.html', {'books': books})





class Qs1View(generic.View):
    def get(self, request, **kwargs):
        return HttpResponse("«Боль неизбежна. Страдание – личный выбор каждого». -Харуки Мураками")


# def qs1(request):
#     return HttpResponse("«Боль неизбежна. Страдание – личный выбор каждого». -Харуки Мураками")





class Qs2View(generic.View):
    def get(self, request, **kwargs):
        return HttpResponse("«Когда счастье есть, о нем не думают» -Чынгыз Айтматов")


# def qs2(request):
#     return HttpResponse("«Когда счастье есть, о нем не думают» -Чынгыз Айтматов")





class Qs3View(generic.View):
    def get(self, request, **kwargs):
        return HttpResponse("«Смысл жизни в том, что она имеет свой конец.»-Франц Кафка")


# def qs3(request):
#     return HttpResponse("«Смысл жизни в том, что она имеет свой конец.»-Франц Кафка")