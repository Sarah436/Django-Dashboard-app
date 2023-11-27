# dashboard/urls.py

from django.urls import path
from .views import dashboard_view  # Make sure the import is correct

urlpatterns = [
    path('', dashboard_view, name='dashboard'),
]
