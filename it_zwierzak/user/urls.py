from django.urls import path, re_path
from user import views

app_name = 'user'


urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('user_profile/', views.profile, name='user_profile'),
    re_path(r'^password/$', views.change, name='change_password'),
    path('confirmation_message/', views.confirmation, name='confirmation_message'),
]
