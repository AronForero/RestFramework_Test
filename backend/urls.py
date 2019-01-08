from django.contrib import admin
from django.urls import path, include
from houses import views

urlpatterns = [
    path('', include('houses.urls')),
    path('admin/', admin.site.urls),
]
