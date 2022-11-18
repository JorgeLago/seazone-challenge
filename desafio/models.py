from django.db import models
from random import randrange

class Imovel(models.Model):
    PET_FRIENDLY = (
        ('S', 'Sim'),
        ('N', 'Não'),
    )

    id_imovel = models.CharField(max_length=10, primary_key=True)
    limite_hospedes = models.IntegerField()
    banheiros = models.IntegerField()
    pet_friendly = models.CharField(max_length=1, choices=PET_FRIENDLY, blank=False, null=False, default='S')
    valor_limpeza = models.FloatField(max_length=10)
    data_ativacao = models.DateField()
    criado_em = models.DateTimeField()
    atualizado_em = models.DateTimeField()

    def __str__(self):
        return self.id_imovel

class Anuncio(models.Model):
    id_imovel = models.CharField(max_length=10, primary_key=True)
    plataforma = models.CharField(max_length=30)
    taxa_plataforma = models.FloatField(max_length=10)
    criado_em = models.DateTimeField()
    atualizado_em = models.DateTimeField()

    def __str__(self):
        return self.id_imovel

class Reserva(models.Model):
    codigo_aleatorio = randrange(0,1000)

    codigo_reserva = models.CharField(max_length=1000, primary_key=True, default=codigo_aleatorio)
    plataforma = models.CharField(max_length=30)
    check_in = models.DateField()
    check_out = models.DateField()
    preco_total = models.FloatField(max_length=10)
    comentarios = models.CharField(max_length=150)
    numero_hospedes = models.IntegerField()
    criado_em = models.DateTimeField()
    atualizado_em = models.DateTimeField()

    def __str__(self):
        return self.codigo_reserva