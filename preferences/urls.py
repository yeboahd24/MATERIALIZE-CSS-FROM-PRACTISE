from django.urls import path
from .views import CustomerForm

app_name = 'preferences'

urlpatterns = [
    path('', CustomerForm.as_view(), name='forms'),
]