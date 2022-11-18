from rest_framework import viewsets
from desafio.models import Imovel, Anuncio, Reserva
from desafio.serializer import ImovelSerializer, AnunciosSerializer, ReservasSerializer

class ImovelViewSet(viewsets.ModelViewSet):
    """Exibindo todos os Imoveis"""
    queryset = Imovel.objects.all()
    serializer_class = ImovelSerializer

class AnunciosSerializer(viewsets.ModelViewSet):
    """Exibindo todos os Anuncios"""
    queryset = Anuncio.objects.all()
    serializer_class = AnunciosSerializer

class ReservasSerializer(viewsets.ModelViewSet):
    """Exibindo todos as Reservas"""
    queryset = Reserva.objects.all()
    serializer_class = ReservasSerializer