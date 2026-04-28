from django.shortcuts import render
from django.http import HttpResponse

def qs1(request):
    return HttpResponse("«Боль неизбежна. Страдание – личный выбор каждого». -Харуки Мураками")

def qs2(request):
    return HttpResponse("«Когда счастье есть, о нем не думают» -Чынгыз Айтматов")

def qs3(request):
    return HttpResponse("«Смысл жизни в том, что она имеет свой конец.»-Франц Кафка")
