from django.urls import path
from . import views

urlpatterns =[

    path('', views.home, name='homepage'),
    path('delete_task/<int:task_id>/', views.delete_task, name="delete_task"),
    path('task_complete/<int:task_id>/', views.task_complete, name="task_complete"),
    path('task_not_complete/<int:task_id>/', views.task_not_complete, name='task_not_complete'),
    path('login/', views.login_profile , name="login"),
    path('register/', views.register, name="register"),
    path('profile/<str:user>/', views.profile, name='profile'),
    path('logout/', views.logout_profile, name='profile'),

]
