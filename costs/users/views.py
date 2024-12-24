from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from costs.users.forms import *
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from costs.users.mixins import RightUserMixin

class LoginPerson(SuccessMessageMixin, LoginView):
    form_class = AuthPersonForm
    template_name = 'users/login.html'
    success_url = reverse_lazy('main')
    login_url = reverse_lazy('users:login')
    success_message = 'Вы авторизованы'
    
    def get_success_url(self):
        return self.success_url
    
class CreatePerson(SuccessMessageMixin, CreateView):
    template_name = 'users/create.html'
    form_class = RegisterPersonForm
    success_url = reverse_lazy('users:login')
    success_message = 'Пользователь создан'
    
def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, 'Пользователь вышел')
        return redirect(reverse_lazy('main'))
    else:
        messages.error(request, 'Вы не авторизованы')
        return redirect(reverse_lazy('main'))
    
    
class PersonUpdate(RightUserMixin, SuccessMessageMixin, UpdateView):
    model = User
    form_class = PersonUpdateForm
    template_name = 'users/update.html'
    success_url = reverse_lazy('main')
    success_message = 'Пользователь изменен'
    login_url = reverse_lazy('users:login')
    
class PersonDelete(RightUserMixin, SuccessMessageMixin, DeleteView):
    model = User
    template_name = 'users/delete.html'
    success_message = 'Пользователь удален'
    login_url = reverse_lazy('users:login')
    success_url = reverse_lazy('main')
    
class PersonShowView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.id == kwargs['pk']:
                return render(request, 'users/show.html', {'user': request.user})
        messages.error(request, 'Необходимо войти')
        return redirect(reverse_lazy('main'))