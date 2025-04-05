# --------------------------- FILE RESPONSIBLE FOR HANDLING THE ROUTERS -------------------------- #

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('app.urls')),                           #pointing to urls in the app 'app'
    path('teste_html/', include('teste_html.urls')),         #pointing to urls in the app 'teste_html'
    path('teste_rest/', include('teste_rest.urls'))             #pointing to urls in the app 'teste_rest'
]
