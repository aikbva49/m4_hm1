from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.views import generic
from django.urls import reverse
from . import models, forms


class RegisterView(generic.CreateView):
    template_name = 'users/register.html'
    form_class = forms.CustomRegisterForm

    def form_valid(self, form):
        print(form.cleaned_data)
        user = form.save()
        login(self.request, user)
        return super(RegisterView, self).form_valid(form=form)

    def get_success_url(self):
        return reverse('user_list')


# def register_view(request):
#     if request.method == "POST":
#         form = forms.CustomRegisterForm(request.POST, request.FILES)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('/user_list/')
#     else:
#         form = forms.CustomRegisterForm()
#     return render(request, 'users/register.html', {'form': form})





class AuthLoginView(generic.FormView):
    template_name = 'users/login.html'
    form_class = forms.CustomLoginForm

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        return super(AuthLoginView, self).form_valid(form=form)

    def get_success_url(self):
        return reverse('user_list')


# def auth_login_view(request):
#     if request.method == "POST":
#         form = forms.CustomLoginForm(data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             return redirect('/user_list/')
#     else:
#         form = forms.CustomLoginForm()
#     return render(request, 'users/login.html', {'form': form})





class AuthLogoutView(generic.View):

    def get(self, request, **kwargs):
        logout(request)
        return redirect(reverse('login'))

    def post(self, request, **kwargs):
        logout(request)
        return redirect(reverse('login'))


# def auth_logout_view(request):
#     logout(request)
#     return redirect('/login/')





class UserListView(generic.ListView):
    template_name = 'users/user_list.html'
    context_object_name = 'us'
    model = models.CustomUser

    def get_queryset(self):
        return self.model.objects.all()


# def user_list_view(request):
#     user_list = models.CustomUser.objects.all()
#     return render(request, 'users/user_list.html', {'us': user_list})