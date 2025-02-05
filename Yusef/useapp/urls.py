from django.urls import path
from .views import index  # Import the correct view

urlpatterns = [
    path('', index, name='index'),  # Ensure this matches the root URL
]
