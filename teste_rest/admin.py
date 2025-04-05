# ------------------- THIS IS TO SHOW THE MODEL PESSOAS INSIDE THE ADMIN PANEL ------------------- #

from django.contrib import admin
from .models import Pessoas

#Editing the visualization of the 'pessoaas' models inside the admin panel
class ListingPessoas(admin.ModelAdmin):
    list_display = ("cod_pessoa","name","age")              #To visualize the info
    list_display_links = ("cod_pessoa","name","age")        #To click in the info
    search_fields= ("name","cod_pessoa",)                   #This has to be a tuple


admin.site.register(Pessoas, ListingPessoas)