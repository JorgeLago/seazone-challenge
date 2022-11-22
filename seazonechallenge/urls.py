from django.contrib import admin
from django.urls import path, include
from desafio.views import ImovelViewSet, AnunciosViewSet, ReservasViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('imoveis', ImovelViewSet, basename='imoveis')
router.register('anuncios', AnunciosViewSet, basename='anuncios')
router.register('reservas', ReservasViewSet, basename='reservas')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]