from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class ToDoModel(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, default=User)
    title = models.CharField(max_length=100, default='')
    content = models.TextField( default='')
    date_created = models.DateTimeField(default=datetime.today)
    target_date = models.DateTimeField(default='')
    mark = models.BooleanField(default=False)


