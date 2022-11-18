from django.contrib import admin
from desafio.models import Imovel

class Imoveis(admin.ModelAdmin):
    list_display = ('id_imovel', 'limite_hospedes', 'banheiros', 'pet_friendly', 'valor_limpeza', 'data_ativacao', 'criado_em', 'atualizado_em')
    list_display_links = ('id_imovel',)
    search_fields = ('id_imovel',)
    list_per_page = 20

admin.site.register(Imovel, Imoveis)