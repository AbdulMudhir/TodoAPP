from django.urls import path
from . import views

urlpatterns =[

    path('profile/<str:user>/delete_task/<int:item_id>/', views.delete_task, name="delete_task"),
    path('profile/<str:user>/task_complete/<int:item_id>/', views.task_complete, name="task_complete"),
    path('profile/<str:user>/task_not_complete/<int:item_id>/', views.task_not_complete, name='task_not_complete'),
    path('login/', views.login_profile , name="login"),
    path('register/', views.register, name="register"),
    path('profile/<str:user>/', views.profile, name='profile'),
    path('logout/', views.logout_profile, name='profile'),
    path('profile/<str:user>/password_change/', views.password_change, name='password_change'),

]
