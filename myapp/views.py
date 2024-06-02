from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from . models import *
from . forms import *
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView






            # List of tasks to do
class TaskList (LoginRequiredMixin,ListView):
    template_name = 'index.html'
    model = Task
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['tasks'] = context['tasks'].filter(user=self.request.user)
        context ['count'] = context['tasks'].filter(complete=False).count()

                # Search function
        search_bar = self.request.GET.get('search') or ''

        if search_bar:
            context['tasks'] = context['tasks'].filter(title__startswith=search_bar)

        context['search_bar'] = search_bar
        return context
            
        
        
    

        # Task Detail
class TaskDetail (DetailView):
    template_name = 'detail.html'
    model = Task
    context_object_name = 'tasks'


        # Add new task
class CreateTask(CreateView):
    model =Task.objects.all()
    form_class = CreateForm
    success_url = reverse_lazy('index')
    template_name = 'create_task.html'

    def form_valid(self, form):
        form.instance.user =  self.request.user
        return super(CreateTask, self).form_valid(form)
           


        # Make changes to task
class UpdateTask (UpdateView):
    model = Task
    template_name =  'update.html'
    fields = ['title', 'description', 'complete' ]
    success_url = reverse_lazy('index')


        # Delete a task
class DeleteTask (DeleteView):
    model  =Task
    context_object_name = 'task'
    success_url = reverse_lazy('index')
    template_name = 'delete.html'









