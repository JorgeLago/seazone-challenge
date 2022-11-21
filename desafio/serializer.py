from rest_framework import serializers
from desafio.models import Imovel, Anuncio, Reserva
from desafio.validators import *

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
    def validate(self, data):
        if not check_in_valido(data['check_in'], data['check_out']):
            raise serializers.ValidationError({'check_in':"O check_in deve ser antes do check_out."})
        return data