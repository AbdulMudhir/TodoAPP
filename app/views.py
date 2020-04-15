from django.shortcuts import render, redirect
from .forms import ToDoForm
from .models import ToDoModel
from datetime import datetime
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistrationForm
from django.contrib.auth.models import User

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


def task_not_complete(request, task_id):
    if request.method == "POST":

        item = ToDoModel.objects.get(id=task_id)
        item.mark = False
        item.save()

        return redirect('/')
    else:
        return redirect('/')


def login(request):
    return render(request, 'app/login.html')


def register(request):

    registered_user = RegistrationForm(request.POST)

    if registered_user.is_valid():

        registered_user.save()

        return redirect('/login/')

    else:
        return render(request, 'app/register.html', {'form': RegistrationForm})


