from django.db import models
from datetime import datetime, date

class Imovel(models.Model):
    PET_FRIENDLY = (
        ('S', 'Sim'),
        ('N', 'Não'),
    )

    imovel_id = models.CharField(max_length=4, primary_key=True)
    limite_hospedes = models.IntegerField()
    banheiros = models.IntegerField()
    pet_friendly = models.CharField(max_length=1, choices=PET_FRIENDLY, blank=False, null=False, default='N')
    valor_limpeza = models.FloatField(max_length=10)
    data_ativacao = models.DateField(auto_now_add=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.imovel_id

class Anuncio(models.Model):
    
    anuncio_id = models.AutoField(primary_key=True)
    imovel_id = models.ForeignKey(Imovel, on_delete=models.CASCADE)
    plataforma = models.CharField(max_length=30)
    taxa_plataforma = models.FloatField(max_length=10)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __int__(self):
        return self.anuncio_id

class Reserva(models.Model):

    reserva_id = models.AutoField(primary_key=True)
    anuncio_id = models.ForeignKey(Anuncio, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    preco_total = models.FloatField(max_length=10)
    comentarios = models.CharField(max_length=150)
    numero_hospedes = models.IntegerField()
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __int__(self):
        return self.reserva_id