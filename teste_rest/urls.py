# ---------------------------- URLS WORKS JUST LIKE CONTROLLERS IN MVC --------------------------- #

from django.urls import path
from .views import create_pessoa

urlpatterns = [
    path('/create', create_pessoa, name='create_pessoa')
]
