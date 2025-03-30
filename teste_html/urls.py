# --------------------------------- ROUTING URLS RELATED TO TEXT --------------------------------- #

from django.urls import path
from teste_html.views import index, template

urlpatterns = [
    path('', index),                    #Using raw html inside the python file
    path('/template', template)          #Using an Hmtl file from templates
]
