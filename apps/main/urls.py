import imp
from django.urls import path

# App modules.
from .views import index

app_name = 'main'

urlpatterns = [
    path('', index, name='index'),
]