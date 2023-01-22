# from django.contrib import admin
from django.urls import path
# from .views import AdoptionApplicationView
from .views import adoption_application_view

from . import views

urlpatterns = [
    path('adopted_animals', views.adopted, name='adopted_animals'),
    path('animals_to_adoption', views.adoptions, name='animals_to_adoption'),
    path('announcement_detail', views.adoption_card, name='announcement_detail'),
    # path('adoption_application', AdoptionApplicationView.as_view(), name='adoption_application')
    path('adoption_application', adoption_application_view, name='adoption_application'),
]
