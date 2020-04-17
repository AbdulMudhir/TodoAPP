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
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text


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

            username = registered_user.cleaned_data['username']
            email = registered_user.cleaned_data['email']
            password = registered_user.cleaned_data['password1']

            user = User.objects.create_user(username=username, email=email, password=password)
            user.is_active = False
            user.save()

            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))

            send_mail("Confirmation Email", f"http://localhost:8000/users/validate/{uid}/{token}",
                      "todolistprojectgit@gmail.com", [email], fail_silently=True)

            return render(request, 'app/activation_email_sent.html')

        else:

            return render(request, 'app/register.html', {'form': registered_user})

    if request.method == "GET":

        if request.user.is_authenticated:
            return redirect('/')

        else:
            return render(request, 'app/register.html', {'form': RegistrationForm})


def activation(request, uidb64, token):
    uid = urlsafe_base64_decode(uidb64)

    user = User.objects.get(pk=uid)

    default_token_generator.check_token(user, token)

    if user and default_token_generator:
        user.is_active = True
        user.save()
        return render(request, 'app/activation_done.html')

    else:
        return redirect('/')
