from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

router.register(r'inmueble', views.inmuebleViewSet)
router.register(r'general', views.generalViewSet)
router.register(r'interior', views.interiorViewSet)
router.register(r'exterior', views.exteriorViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
