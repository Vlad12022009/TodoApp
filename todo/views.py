from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateTaskModelForm
from .models import CreateTask
from django.views.generic import ListView
from django.views.generic.edit import FormMixin
from django.urls import reverse
# Create your views here.

class IndexListView(ListView, FormMixin):
    model = CreateTask
    paginate_by = 4
    context_object_name = 'tasks'
    template_name = 'todo/index.html'
    form_class = CreateTaskModelForm
    def get_success_url(self):
        return reverse('index')
    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            form.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if CreateTask.objects.filter(status=True):
            context['delete_complete_tasks'] = True
        return context

def status_reverse(request, pk):
    obj = get_object_or_404(CreateTask, pk=pk)
    obj.status = not obj.status
    obj.save()
    return redirect("/")

def delete_complete_tasks(request):
    tasks = CreateTask.objects.filter(status=True)
    if request.method == 'POST':
        for i in tasks:
            i.delete()
        return redirect("/")
    context = {
        "tasks": tasks
    }
    return render(request, "todo/delete_complete_tasks.html", context=context)

def update_task(request, pk):
    obj = get_object_or_404(CreateTask, pk=pk)
    form = CreateTaskModelForm(None, instance=obj)
    if request.method == "POST":
        form = CreateTaskModelForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            return redirect("/")
    context = {
        'form': form
    }
    return render(request, 'todo/update_task.html', context=context)

def delete_task(request, pk):
    task = get_object_or_404(CreateTask, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect("/")
    context = {
        "task": task
   
    }
    return render(request, "todo/delete_complete_tasks.html", context=context)