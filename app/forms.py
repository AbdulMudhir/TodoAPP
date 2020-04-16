from .models import ToDoModel
from django import forms
from .widgets import DateTimePicker
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
import datetime


class PasswordChangeForms(PasswordChangeForm):

    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'})
                                 )
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    error_messages = {

        'password_incorrect': ("Your old password was incorrect."),
        'password_mismatch':'The two password fields didn’t match.',
    }
    class Meta:

        model = User

        fields = (
                  'old_password',
                  'new_password1',
                  'newpassword2',
        )



class ToDoForm(forms.ModelForm):
    date_now = datetime.datetime.utcnow().strftime('%Y-%m-%d')

    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                          'onkeyup':"textCounter(this,'counter',100);",
                                                          'id':'message'
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

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("The email has already been used.")

        else:
            return email


    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user