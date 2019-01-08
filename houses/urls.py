from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from rest_framework_swagger.views import get_swagger_view

#Creamos la instancia del Router que usaremos para automatizar los URL
router = DefaultRouter()

#Registramos las vistas
router.register(r'inmueble', views.inmuebleViewSet)
router.register(r'general', views.generalViewSet)
router.register(r'interior', views.interiorViewSet)
router.register(r'exterior', views.exteriorViewSet)

#creamos la instancia de swagger para automatizar la documentacion
schema_view = get_swagger_view(title='Pastebin API')

#Creamos nuestro patron de urls
urlpatterns = [
    path('api/doc/', schema_view),
    path('', include(router.urls)),
]
