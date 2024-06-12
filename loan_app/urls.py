#hashroot_project/loan_app/urls.py

from django.urls import path
from .views import *


urlpatterns = [

    path('', home, name='home'),
]

