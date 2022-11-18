from rest_framework import viewsets
from desafio.models import Imovel
from desafio.serializer import ImovelSerializer

class ImovelViewSet(viewsets.ModelViewSet):
    """Exibindo todos os Imoveis"""
    queryset = Imovel.objects.all()
    serializer_class = ImovelSerializer