from django.urls import path
from . import views



urlpatterns = [
    path('my_profile', views.my_profile, name='my_profile'),
    path('favourite', views.favourite, name='favourite'),
    path('adoptions', views.adoptions, name='adoptions'),
    path('user_data', views.user_data, name='user_data')
]





