from django.db import models

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

