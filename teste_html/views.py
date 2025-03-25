# ---------------------------- VIEW IS RESPOSIBLE FOR RENDER THE HTML ---------------------------- #

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

#Using raw html
def index(request):
    return HttpResponse(
        """
        <h1>Teste renderizando HTML</h1>    
        <p>Esse Html foi renderizado pelo próprio Django</p>   
        """
    )

#Using templates, full html file
def template(request):
    return render(request, 'teste.html')