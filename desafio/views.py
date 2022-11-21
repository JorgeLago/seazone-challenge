from rest_framework import viewsets, filters
from desafio.models import Imovel, Anuncio, Reserva
from desafio.serializer import ImovelSerializer, AnunciosSerializer, ReservasSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView

class ImovelViewSet(viewsets.ModelViewSet):
    """Exibindo todos os Imoveis"""
    queryset = Imovel.objects.all()
    serializer_class = ImovelSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    search_fields = ['id_imovel']
    ordering_fields = ['id_imovel']

class AnunciosSerializer(viewsets.ModelViewSet):
    """Exibindo todos os Anuncios"""
    queryset = Anuncio.objects.all()
    serializer_class = AnunciosSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    search_fields = ['id_anuncio']
    ordering_fields = ['id_anuncio']

class ReservasSerializer(viewsets.ModelViewSet):
    """Exibindo todos as Reservas"""
    queryset = Reserva.objects.all()
    serializer_class = ReservasSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    search_fields = ['id_reserva']
    ordering_fields = ['id_reserva']