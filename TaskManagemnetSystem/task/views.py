from django.shortcuts import render,redirect
from task.forms import TaskForm
# Create your views here.
def addTask(request):
    if request.method =="POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('addTask')
    else:
        form = TaskForm()
    return render(request, 'addTask.html', {'form': form})