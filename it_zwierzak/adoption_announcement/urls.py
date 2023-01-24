from django.urls import path
from .views import adoption_application_view
from .models import Announcement
from . import views

urlpatterns = [
    path('adopted_animals', views.adopted, name='adopted_animals'),
    path('animals_for_adoption', views.adoptions, name='animals_for_adoption'),
    path('announcement_detail', views.adoption_card, name='announcement_detail'),
    path('adoption_application', adoption_application_view, name='adoption_application'),
]
