from rest_framework import viewsets, filters
from desafio.models import Imovel, Anuncio, Reserva
from desafio.serializer import ImovelSerializer, AnunciosSerializer, ReservasSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class ImovelViewSet(viewsets.ModelViewSet):
    """Exibindo todos os Imoveis"""
    queryset = Imovel.objects.all()
    serializer_class = ImovelSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    search_fields = ['imovel_id']
    ordering_fields = ['imovel_id']

class AnunciosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os Anuncios"""
    queryset = Anuncio.objects.all()
    serializer_class = AnunciosSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    search_fields = ['anuncio_id']
    ordering_fields = ['anuncio_id']
    http_method_names = ['get','post', 'put', 'path']

class ReservasViewSet(viewsets.ModelViewSet):
    """Exibindo todos as Reservas"""
    queryset = Reserva.objects.all()
    serializer_class = ReservasSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    search_fields = ['reserva_id']
    ordering_fields = ['reserva_id']
    http_method_names = ['get','post', 'delete']