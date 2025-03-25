# --------------------------- FILE RESPONSIBLE FOR HANDLING THE ROUTERS -------------------------- #

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('teste_html', include('teste_html.urls'))
]
