from datetime import datetime

from django.http import HttpRequest
from django.contrib.auth import logout, login, authenticate, update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordResetForm
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .forms import RegistrationForm, PasswordChangeForms
from .forms import ToDoForm
from .models import ToDoModel


# Create your views here.


def password_change(request, user):
    if request.method == "POST":

        form = PasswordChangeForms(user=request.user, data=request.POST)

        if form.is_valid():

            form.save()
            update_session_auth_hash(request, form.user)

            return redirect('/')

        else:
            return render(request, 'app/password_change.html', {'form': form})

    if request.method == "GET":

        if request.user.is_authenticated:
            return render(request, 'app/password_change.html', {'form': PasswordChangeForms(user=request.user)})

        else:
            return render(request, 'app/password_change.html', {'form': PasswordChangeForms(user=request.user)})


def delete_task(request, item_id, user):
    if request.method == "POST":
        task = ToDoModel.objects.get(username_id=request.user.id, id=item_id)

        task.delete()
        return redirect(f'/profile/{request.user}/')

    if request.method == "GET":

        if request.user.is_authenticated:

            return redirect(f'/profile/{request.user}/')

        else:

            return redirect('/login')


def task_complete(request, item_id, user):
    if request.method == "POST":
        item = ToDoModel.objects.get(username_id=request.user.id, id=item_id)
        item.mark = True
        item.save()

        return redirect(f'/profile/{request.user}/')

    if request.method == "GET":

        if request.user.is_authenticated:

            return redirect(f'/profile/{request.user}/')

        else:

            return redirect('/login')


def logout_profile(request):
    if request.method == "POST":
        logout(request)
        return redirect('/')


def task_not_complete(request, item_id, user):
    if request.method == "POST":
        item = ToDoModel.objects.get(username_id=request.user.id, id=item_id)
        item.mark = False
        item.save()

        return redirect(f'/profile/{request.user}/')

    if request.method == "GET":

        if request.user.is_authenticated:

            return redirect(f'/profile/{request.user}/')

        else:

            return redirect('/login')


def login_profile(request):
    if request.method == "POST":

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            return redirect('/')

        else:
            return render(request, 'app/login.html', {'error': 'Username or Password is incorrect'})

    if request.method == "GET":

        if request.user.is_authenticated:
            return redirect('/')

        else:
            return render(request, 'app/login.html')


def profile(request, user):
    users_to_do_list = ToDoModel.objects.filter(username_id=request.user.id).order_by('mark', '-date_created')

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

            return redirect(f'/profile/{request.user}/')

        else:
            return redirect(f'/profile/{request.user}/', form)

    if request.method == "GET":

        if not request.user.is_authenticated:
            return redirect('/login')
        else:
            return render(request, 'app/profile.html', data)


def register(request):
    if request.method == "POST":

        registered_user = RegistrationForm(request.POST)

        if registered_user.is_valid():

            registered_user.save()
            messages.success(request, 'Your account has been created successfully.')
            return redirect('/login')

        else:

            return render(request, 'app/register.html', {'form': registered_user})

    if request.method == "GET":

        if request.user.is_authenticated:
            return redirect('/')

        else:
            return render(request, 'app/register.html', {'form': RegistrationForm})


# def password_reset(request):
#     if request.method == "POST":
#         email = request.POST['email']
#
#         form = PasswordResetForm({'email': email})
#
#         if form.is_valid():
#
#             if User.objects.filter(email__iexact=email).exists():
#
#                 form.send_mail(subject_template_name="app/login.html",
#                                from_email="todolistprojectgit@gmail.com",
#                                to_email=email,
#                                context=None,
#                                email_template_name="app/login.html")
#
#                 #form.save()
#
#
#
#
#         return redirect('/forgot_password/done')
#     return render(request, 'app/password_reset.html')
#
# def password_reset_sent(request):
#
#     return render(request, 'app/password_reset_sent.html')
