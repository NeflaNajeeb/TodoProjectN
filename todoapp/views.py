from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView

from .forms import TodoForm
from .models import Task


# Create your views here.

class TaskListView(ListView):
    model=Task
    template_name ='home.html'
    context_object_name = 'task'

class TaskDetailView(DetailView):
    model=Task
    template_name = 'detailList.html'
    context_object_name = 'task'

class TaskUpdateView(UpdateView):
    model=Task
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('name','priority','date')

    def get_success_url(self):
        return reverse_lazy('TaskDetailView',kwargs={'pk':self.object.id})

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('TaskListView')

def add(request):
    task1=Task.objects.all()
    if request.method=='POST':
        name=request.POST.get("task")
        priority=request.POST.get("priority")
        date=request.POST.get("date")
        task=Task(name=name,priority=priority,date=date)
        task.save()
    return render(request,'home.html',{'task':task1})
def delete(request,id):
    task=Task.objects.get(id=id)
    if request.method=="POST":
        task.delete()
        return redirect('/')
    return render(request,'delete.html')
def update(request,id):
    task=Task.objects.get(id=id)
    f=TodoForm(request.POST or None,instance=task)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request,'edit.html',{'f':f,'task':task})

