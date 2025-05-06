from django.contrib import admin
from django.urls import path
from galeria.views import index #do arquivo views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index)
]
