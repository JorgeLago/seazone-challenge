from django.contrib import admin
from django.urls import path, include
from desafio.views import ImovelViewSet, AnunciosSerializer, ReservasSerializer
from rest_framework import routers

router = routers.DefaultRouter()
router.register('imoveis', ImovelViewSet, basename='imoveis')
router.register('anuncios', AnunciosSerializer, basename='anuncios')
router.register('reservas', ReservasSerializer, basename='reservas')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]