from django.db import models

class Imovel(models.Model):
    id_imovel = models.CharField(max_length=10, primary_key=True)
    limite_hospedes = models.IntegerField(max_length=10)
    banheiros = models.IntegerField(max_length=10)
    pet_friendly = models.BooleanField()
    valor_limpeza = models.FloatField(max_length=10)
    data_ativacao = models.DateField()
    criado_em = models.DateTimeField()
    atualizado_em = models.DateTimeField()

    class imovel(object):
        def __init__(self, id_imovel, limite_hospedes, banheiros, pet_friendly, valor_limpeza, data_ativacao, criado_em, atualizado_em)
            self.id_movel = id_imovel
            self.limite = limite_hospedes
            self.banheiros = banheiros
            self.pet_friendly = pet_friendly
            self.valor_limpeza = valor_limpeza
            self.data_ativacao = data_ativacao
            self.criado_em = criado_em
            self.atualizado_em = atualizado_em

