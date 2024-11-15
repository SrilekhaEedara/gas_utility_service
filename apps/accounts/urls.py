from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),  # Corrected function name
    path('login/', views.login_view, name='login'),           # Corrected function name
]

