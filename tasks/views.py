from django.shortcuts import render
from django.views.generic import ListView

from tasks.models import Task


class TaskList(ListView):
    model = Task
    template_name = 'base/task_list.html'
    context_object_name = 'tasks'

