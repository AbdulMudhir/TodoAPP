from django.urls import path, re_path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('profile/<str:user>/delete_task/<int:item_id>/', views.delete_task, name="delete_task"),
    path('profile/<str:user>/task_complete/<int:item_id>/', views.task_complete, name="task_complete"),
    path('profile/<str:user>/task_not_complete/<int:item_id>/', views.task_not_complete, name='task_not_complete'),
    path('login/', views.login_profile, name="login"),
    path('register/', views.register, name="register"),
    path('profile/<str:user>/', views.profile, name='profile'),
    path('logout/', views.logout_profile, name='profile'),
    path('profile/<str:user>/password_change/', views.password_change, name='password_change'),
    re_path(r'^users/validate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',views.activation, name='activate'),

    path('password_reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='app/password_reset_sent.html'),
         name='password_reset_done'),

    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='app/password_reset.html/'),
         name='password_reset_confirm'),

    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='app/password_reset_form.html'),
         name='password_reset'),

    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='app/password_reset_done.html'),
         name='password_reset_complete'),

]
