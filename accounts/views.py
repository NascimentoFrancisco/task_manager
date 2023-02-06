from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
        CreateView, UpdateView, DeleteView, View
    )
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin

from .models import User
from .forms import CreationUserForm, ChangeUserForm


class ProfileUser(View):


    def get(self, request):
        return render(request, 'accounts/profile.html')
        

class LoginUser(LoginView):


    template_name = 'accounts/login.html'

    def form_valid(self, form):
        user = form.get_user()
        messages.success(self.request, f'Bem vindo {user}')
        return super().form_valid(form)


class LogoutUser(LogoutView):
    
    
    template_name = 'base.html'

    def get_success_url_allowed_hosts(self):
        messages.info(self.request,'Até breve!')
        return super().get_success_url_allowed_hosts()


class CreateUser(CreateView):

    
    model = User
    template_name = 'accounts/create.html'
    form_class = CreationUserForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        messages.success(
            self.request,'Cadastro realizado com sucesso! Faça seu login.'
        )
                
        return super().form_valid(form)


class UpdateUser(LoginRequiredMixin, UpdateView):


    model = User
    login_url = reverse_lazy('accounts:login_user')
    template_name = 'accounts/create.html'
    form_class = ChangeUserForm
    success_url = reverse_lazy('accounts:home_user')

    def get_object(self):
        return self.request.user
    
    def form_valid(self, form):
        messages.success(self.request, 
            f'{self.get_object().name} alterado com sucesso!'
        )
        return super().form_valid(form)


class DeleteUser(LoginRequiredMixin, DeleteView):


    model = User
    login_url = reverse_lazy('accounts:login_user')
    template_name = 'accounts/delete.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user

    def get_success_url(self):
        
        messages.success(self.request,
            'Perfil apagado com sucesso!'
        )
        return super().get_success_url()


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    
    
    template_name = 'accounts/password_reset.html'
    email_template_name = 'accounts/password_reset_email.html'
    subject_template_name = 'accounts/password_reset_subject'
    success_message = "Enviamos um e-mail com instruções para definir sua senha, " \
                       "se existir uma conta com o e-mail que você digitou. Você deve recebê-lo em breve." \
                       "Se você não receber um e-mail, " \
                       "certifique-se de que inseriu o endereço com o qual se registrou e verifique sua pasta de spam."
    success_url = reverse_lazy('home')