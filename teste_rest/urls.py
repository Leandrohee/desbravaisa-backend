# ---------------------------- URLS WORKS JUST LIKE CONTROLLERS IN MVC --------------------------- #

from django.urls import path
from .views import create_pessoa, get_pessoas, index, detail_pessoa

urlpatterns = [
    path('',index, name='index'),
    path('create', create_pessoa, name='create_pessoa'),
    path('get', get_pessoas, name='get_pessoas'),
    path('get/<int:pk>', detail_pessoa, name='detail_pessoa')
]
