from rest_framework import serializers
from desafio.models import Imovel, Anuncio, Reserva

class ImovelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imovel
        fields = '__all__'

class AnunciosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anuncio
        fields = '__all__'

class ReservasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = '__all__'