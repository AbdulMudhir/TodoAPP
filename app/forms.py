from .models import ToDoModel
from django import forms
from .widgets import DateTimePicker
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import datetime


date_now = datetime.datetime.utcnow().strftime('%Y-%m-%d')



class ToDoForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                              }), required=True)
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control',
                                                              }), required=True)

    target_date = forms.DateTimeField(widget=forms.DateInput(attrs={'class': 'form-control',
                                                                    'type':'date',
                                                                    'value':date_now,
                                                                    'min':date_now,
                                                              }), required=True)



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
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control',
                                                              }), required=True)
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                             }), required=True, max_length=25)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                              }), required=True)
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                              }), required=True)



    class Meta:
        model = User

        fields = (

            'username',
            'password1',
            'password2',
            'email',

        )
