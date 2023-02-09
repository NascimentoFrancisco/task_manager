from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
        CreateView, ListView,UpdateView, DeleteView
    )

from .models import Task
from .forms import CreateUpdadteTask
# Create your views here.


class CreateTasks(LoginRequiredMixin, CreateView):


    model = Task
    login_url = reverse_lazy('accounts:login_user')
    template_name = 'tasks/create.html'
    form_class = CreateUpdadteTask
    success_url = reverse_lazy('tasks:home_tasks')

    def form_valid(self, form):
        
        form.instance.user = self.request.user
        title = form.data['title']

        messages.success(self.request, 
            f'Tarefa "{title}" criada com sucesso!'
        )
        return super().form_valid(form)


class ListTasks(LoginRequiredMixin, ListView):
    

    template_name = 'tasks/list.html'
    login_url = reverse_lazy('accounts:login_user')

    def get_queryset(self):
        queryset = Task.objects.filter(user = self.request.user).order_by('status')
        return queryset


class UpdateTasks(LoginRequiredMixin, UpdateView):


    login_url = reverse_lazy('accounts:login_user')
    model = Task
    template_name = 'tasks/create.html'
    form_class = CreateUpdadteTask
    success_url = reverse_lazy('tasks:home_tasks')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar Tarefa'
        return context

    def get_success_url(self) -> str:
        messages.success(self.request, 
            f'Tarefa "{self.get_object().title}" alterada com sucesso!'
        )
        return super().get_success_url()


class FinishTasks(LoginRequiredMixin, UpdateView):


    login_url = reverse_lazy('accounts:login_user')
    model = Task
    template_name = 'tasks/finish.html'
    fields = []
    success_url = reverse_lazy('tasks:home_tasks')

    def form_valid(self, form):

        now = timezone.now()
        
        form.instance.status = True
        form.instance.date_conclusion = now
                
        if now <= self.get_object().deadline_date:
            form.instance.punctuality = True
        
        return super().form_valid(form)

    def get_success_url(self) -> str:

        messages.success(self.request, 
            f'Tarefa "{self.get_object().title}" finalizada com sucesso!'
        )

        return super().get_success_url()


class DeleteTasks(LoginRequiredMixin, DeleteView):


    model = Task
    login_url = reverse_lazy('accounts:login_user')
    template_name = 'tasks/delete.html'
    success_url = reverse_lazy('tasks:home_tasks')

    def get_success_url(self):
        
        messages.success(self.request,
            f'Tarefa "{self.get_object().title}" apagada com sucesso!'
        )
        return super().get_success_url()