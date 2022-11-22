from rest_framework import viewsets, filters
from desafio.models import Imovel, Anuncio, Reserva
from desafio.serializer import ImovelSerializer, AnunciosSerializer, ReservasSerializer
from django_filters.rest_framework import DjangoFilterBackend

class ImovelViewSet(viewsets.ModelViewSet):
    """Exibindo todos os Imoveis"""
    queryset = Imovel.objects.all()
    serializer_class = ImovelSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    search_fields = ['imovel_id']
    ordering_fields = ['imovel_id']

class AnunciosSerializer(viewsets.ModelViewSet):
    """Exibindo todos os Anuncios"""
    queryset = Anuncio.objects.all()
    serializer_class = AnunciosSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    search_fields = ['anuncio_id']
    ordering_fields = ['anuncio_id']
    http_method_names = ['get','post', 'put', 'path']

class ReservasSerializer(viewsets.ModelViewSet):
    """Exibindo todos as Reservas"""
    queryset = Reserva.objects.all()
    serializer_class = ReservasSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    search_fields = ['reserva_id']
    ordering_fields = ['reserva_id']
    http_method_names = ['get','post', 'delete']