from django.shortcuts import render, redirect
from .forms import ToDoForm
from .models import ToDoModel
from datetime import datetime


# Create your views here.


def home(request):
    data = {'form': ToDoForm,
            'data': ToDoModel.objects.all().order_by('mark'),
            'today': datetime.today()}

    if request.method == "POST":

        form = ToDoForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/')

    return render(request, 'app/home.html', data)


def delete_task(request, task_id):
    if request.method == "POST":

        form = ToDoModel.objects.get(id=task_id)
        form.delete()

        return redirect('/')

    else:
        return redirect('/')


def task_complete(request, task_id):

    if request.method == "POST":

        item = ToDoModel.objects.get(id=task_id)
        item.mark = True
        item.save()

        return redirect('/')
    else:
        return redirect('/')
