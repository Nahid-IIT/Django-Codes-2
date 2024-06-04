from django.shortcuts import render,redirect
from  task.models import Task
from task.forms import TaskForm
def home(request):
    return render(request, 'base.html')

def showTask(request):
   data = Task.objects.all()
   return render(request, 'showTask.html', {'data': data})

def editTask(request, id):
    task = Task.objects.get(pk=id)
    form = TaskForm(instance=task)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('showTask')
    return render(request, 'addTask.html',{'form': form})
        

def deleteTask(request,id):
    task  = Task.objects.get(pk=id).delete()
    return redirect('showTask')