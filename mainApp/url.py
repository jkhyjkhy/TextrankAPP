from django.urls import path

from .views import *

app_name = "mainApp"

urlpatterns = [
    path('', summarize_view, name='summarize'),
]