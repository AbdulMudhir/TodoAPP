from django.shortcuts import render, redirect
from .forms import ToDoForm
from .models import ToDoModel
from datetime import datetime
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistrationForm
from django.contrib.auth.models import User


# Create your views here.


def home(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return render(request, 'app/home.html', {'user': request.user})

        else:
            return render(request, 'app/home.html')


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
    if request.method == "GET":

        if request.user.is_authenticated:
            return redirect(f'/profile/{request.user.username}/')

    return render(request, 'app/login.html')


def profile(request, user_id):
    data = {'form': ToDoForm,
            'data': ToDoModel.objects.all().order_by('mark'),
            'today': datetime.today()}

    if request.method == "POST":
        form = ToDoForm(request.POST)

        if form.is_valid():
            # populating the user id that is logged in
            current_form = form.save(commit=False)
            current_form.username_id = request.user.id

            current_form.save()

            return redirect(f'/profile/{user_id}/')

    return render(request, 'app/profile.html', data)


def register(request):
    if request.method == "POST":

        registered_user = RegistrationForm(request.POST)

        if registered_user.is_valid():

            registered_user.save()

            return redirect('/login/')

        else:

            return render(request, 'app/register.html', {'form': registered_user})



    else:
        return render(request, 'app/register.html', {'form': RegistrationForm})
