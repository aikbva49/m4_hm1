from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from . import models, forms

def register_view(request):
    if request.method == "POST":
        form = forms.CustomRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/user_list/')
    else:
        form = forms.CustomRegisterForm()
    return render(request, 'users/register.html', {'form': form})

def auth_login_view(request):
    if request.method == "POST":
        form = forms.CustomLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/user_list/')
    else:
        form = forms.CustomLoginForm()
    return render(request, 'users/login.html', {'form': form})

def auth_logout_view(request):
    logout(request)
    return redirect('/login/')

def user_list_view(request):
    user_list = models.CustomUser.objects.all()
    return render(request, 'users/user_list.html', {'us': user_list})