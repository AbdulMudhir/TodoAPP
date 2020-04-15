from .models import ToDoModel
from django import forms
from .widgets import DateTimePicker
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ToDoForm(forms.ModelForm):
    title = forms.CharField(required=True)
    content = forms.CharField(required=True)
    target_date = forms.DateTimeField(required=True, widget=DateTimePicker())

    class Meta:
        model = ToDoModel
        widgets = {
            'target_date': DateTimePicker
        }

        fields = [

            'title',
            'content',
            'target_date',

        ]


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    username = forms.CharField(widget=forms.TextInput(attrs={'class': '',
                                                             'placeholder': 'Username'
                                                             }), required=True)
    password1 = forms.CharField(widget=forms.TextInput(attrs={'class': '',
                                                              'placeholder': 'Password'
                                                              }), required=True)
    password2 = forms.CharField(widget=forms.TextInput(attrs={'class': '',
                                                              'placeholder': 'Confirm Password'
                                                              }), required=True)

    class Meta:
        model = User

        fields = (

            'username',
            'password1',
            'password2',
            'email',

        )
