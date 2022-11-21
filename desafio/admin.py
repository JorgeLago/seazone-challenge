from django.contrib import admin
from desafio.models import Imovel, Anuncio, Reserva

class Imoveis(admin.ModelAdmin):
    list_display = ('imovel_id', 'limite_hospedes', 'banheiros', 'pet_friendly', 'valor_limpeza', 'data_ativacao', 'criado_em', 'atualizado_em')
    list_display_links = ('imovel_id',)
    search_fields = ('imovel_id',)
    list_per_page = 20

admin.site.register(Imovel, Imoveis)

class Anuncios(admin.ModelAdmin):
    list_display = ('anuncio_id', 'imovel_id', 'plataforma', 'taxa_plataforma', 'criado_em', 'atualizado_em')
    list_display_links = ('anuncio_id',)
    search_fields = ('anuncio_id',)
    list_per_page = 20

admin.site.register(Anuncio, Anuncios)

class Reservas(admin.ModelAdmin):
    list_display = ('reserva_id', 'anuncio_id', 'check_in', 'check_out', 'preco_total', 'comentarios', 'numero_hospedes', 'criado_em', 'atualizado_em')
    list_display_links = ('reserva_id',)
    search_fields = ('reserva_id',)
    list_per_page = 20

admin.site.register(Reserva, Reservas)