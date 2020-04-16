from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns =[

    path('profile/<str:user>/delete_task/<int:item_id>/', views.delete_task, name="delete_task"),
    path('profile/<str:user>/task_complete/<int:item_id>/', views.task_complete, name="task_complete"),
    path('profile/<str:user>/task_not_complete/<int:item_id>/', views.task_not_complete, name='task_not_complete'),
    path('login/', views.login_profile , name="login"),
    path('register/', views.register, name="register"),
    path('profile/<str:user>/', views.profile, name='profile'),
    path('logout/', views.logout_profile, name='profile'),
    path('profile/<str:user>/password_change/', views.password_change, name='password_change'),


    path('password_reset/done/',auth_views.PasswordResetCompleteView.as_view(template_name='app/password_reset_sent.html'),name='password_reset_done'),


    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='app/password_change.html/'), name='password_reset_confirm'),

    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='app/password_reset_form.html'), name='password_reset'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='app/password_change.html'), name='password_change'),


    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),name='password_reset_complete'),


]
