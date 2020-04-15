from django.shortcuts import render, redirect
from .forms import ToDoForm
from .models import ToDoModel
from datetime import datetime
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistrationForm
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate


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


def logout_profile(request):
    if request.method == "POST":
        logout(request)
        return redirect('/')


def task_not_complete(request, task_id):
    if request.method == "POST":

        item = ToDoModel.objects.get(id=task_id)
        item.mark = False
        item.save()

        return redirect('/')
    else:
        return redirect('/')


def login_profile(request):
    if request.method == "POST":

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            return redirect('/')

        else:
            print(user)
            return render(request, 'app/login.html', {'error': 'Username or Password is incorrect'})

    return render(request, 'app/login.html')


def profile(request, user):

    users_to_do_list = ToDoModel.objects.filter(username_id=request.user.id).order_by('mark')

    data = {'form': ToDoForm,
            'data': users_to_do_list,
            'today': datetime.today()}

    if request.method == "POST":
        form = ToDoForm(request.POST)

        if form.is_valid():
            # populating the user id that is logged in
            current_form = form.save(commit=False)
            current_form.username_id = request.user.id

            current_form.save()

            return redirect(f'/profile/{user}/')

    if request.method == "GET":

        if not request.user.is_authenticated:
            return redirect('/login')
        else:
            return redirect(f'/profile/{user}/')



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
