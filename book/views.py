from django.shortcuts import render
from django.http import HttpResponse

def q1(request):
    return HttpResponse("«Боль неизбежна. Страдание – личный выбор каждого». -Харуки Мураками")

def q2(request):
    return HttpResponse("«Когда счастье есть, о нем не думают» -Чынгыз Айтматов")

def q3(request):
    return HttpResponse("«Смысл жизни в том, что она имеет свой конец.»-Франц Кафка")
