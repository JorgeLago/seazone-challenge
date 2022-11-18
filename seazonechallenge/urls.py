from django.contrib import admin
from django.urls import path, include
from desafio.views import ImovelViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('imoveis', ImovelViewSet, basename='imoveis')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]