from django.urls import path, include
from . import views

app_name = 'accounts'

urlpatterns = [
        path('signup/', views.SignUp.as_view(), name='signup'),
        path('<int:pk>/', views.user_detail, name='user_detail'),
        path("edit/<int:pk>/", views.edit_user_profile, name="user_edit"),
]
