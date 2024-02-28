from django.shortcuts import render, redirect
from first_app.forms import TaskForm
from first_app.models import TaskModel

def base(request):
    return render(request, 'base.html')

def add_task(request):
    if request.method == 'POST':
        task = TaskForm(request.POST)
        if task.is_valid():
            task.save()
            print(task.cleaned_data)
            return redirect('show_task')
    else:
        task = TaskForm()
    return render(request, 'add_task.html', {'task': task})

def show_task(request):
    tasks = TaskModel.objects.all()
    for task in tasks:
        print(task.taskTitle) 

    return render(request, 'show_task.html', {'data': tasks})

def edit_task(request, id):
    task = TaskModel.objects.get(pk=id)
    form = TaskForm(instance=task)
    
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            return redirect('show_task')
    else:
        form = TaskForm(instance=task)  
    
    return render(request, 'add_task.html', {'task': form})


def delete_task(request,id):
    task=TaskModel.objects.get(pk = id).delete()
    return redirect('show_task')
def complete(request,id):
    task=TaskModel.objects.get(pk = id).delete()
    return redirect('show_task')
