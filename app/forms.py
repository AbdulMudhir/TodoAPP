from .models import ToDoModel
from django import forms
from .widgets import DateTimePicker


class ToDoForm(forms.ModelForm):

    title = forms.CharField(required=True)
    content = forms.CharField(required=True)
    target_date = forms.DateTimeField(required=True, widget=DateTimePicker())


    class Meta:
        model = ToDoModel
        widgets = {
            'target_date': DateTimePicker
        }

        fields =[

            'title',
            'content',
            'target_date',


        ]


