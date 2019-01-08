from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from rest_framework_swagger.views import get_swagger_view

router = DefaultRouter()

router.register(r'inmueble', views.inmuebleViewSet)
router.register(r'general', views.generalViewSet)
router.register(r'interior', views.interiorViewSet)
router.register(r'exterior', views.exteriorViewSet)

schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    path('api/doc/', schema_view),
    path('', include(router.urls)),
]
