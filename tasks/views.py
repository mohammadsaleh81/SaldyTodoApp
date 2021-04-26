from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from tasks.models import Task


class CustomLoginView(LoginView):
    template_name = 'tasks/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')


class TaskList(LoginRequiredMixin,ListView):
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(complete=False).count()
        return context


class TaskDetail(LoginRequiredMixin,DetailView):
    model = Task
    template_name = 'tasks/task.html'

class TaskCreate(LoginRequiredMixin,CreateView):
    model = Task
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('tasks:tasks')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)



class TaskUpdate(LoginRequiredMixin,UpdateView):
    model = Task
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('tasks:tasks')


class TaskDelete(LoginRequiredMixin,DeleteView):
    model = Task
    success_url = reverse_lazy('tasks:tasks')
    context_object_name = 'task'
