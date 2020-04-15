from django.urls import path
from . import views

urlpatterns =[

    path('', views.home, name='homepage'),
    path('delete_task/<int:task_id>/', views.delete_task, name="delete_task"),
    path('task_complete/<int:task_id>/', views.task_complete, name="task_complete")


]
