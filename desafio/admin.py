from django.contrib import admin
from desafio.models import Imovel, Anuncio, Reserva

class Imoveis(admin.ModelAdmin):
    list_display = ('id_imovel', 'limite_hospedes', 'banheiros', 'pet_friendly', 'valor_limpeza', 'data_ativacao', 'criado_em', 'atualizado_em')
    list_display_links = ('id_imovel',)
    search_fields = ('id_imovel',)
    list_per_page = 20

admin.site.register(Imovel, Imoveis)

class Anuncios(admin.ModelAdmin):
    list_display = ('id_imovel', 'plataforma', 'taxa_plataforma', 'criado_em', 'atualizado_em')
    list_display_links = ('plataforma',)
    search_fields = ('plataforma',)
    list_per_page = 20

admin.site.register(Anuncio, Anuncios)

class Reservas(admin.ModelAdmin):
    list_display = ('codigo_reserva', 'plataforma', 'check_in', 'check_out', 'preco_total', 'comentarios', 'numero_hospedes', 'criado_em', 'atualizado_em')
    list_display_links = ('codigo_reserva',)
    search_fields = ('codigo_reserva',)
    list_per_page = 20

admin.site.register(Reserva, Reservas)