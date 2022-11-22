from rest_framework.test import APITestCase
from desafio.models import Imovel, Reserva, Anuncio

class ImovelModelTestCase(APITestCase):

    def setUp(self):
        self.imovel = Imovel (
            imovel_id = '2234',
            limite_hospedes = '13',
            banheiros = '3',
        )
        
    def test_verifica_atributos_do_imovel(self):
        """Teste verificador de atributos do imovel """
        self.assertEquals(self.imovel.imovel_id, '2234')
        self.assertEquals(self.imovel.limite_hospedes, '13')
        self.assertEquals(self.imovel.banheiros, '3')
        self.assertEquals(self.imovel.pet_friendly, 'N')
        self.assertEquals(self.imovel.valor_limpeza, '120.0')
        self.assertEquals(self.imovel.data_ativacao, '2022-6-22')
        self.assertEquals(self.imovel.criado_em, '2022-6-22')
        self.assertEquals(self.imovel.atualizado_em, '2022-6-22')


# class AnuncioTestCase(APITestCase):
    
#         def setUp(self):
#             self.list_url = reverse('anuncios-list')
            
#             self.anuncio_1 = Anuncio (
#                 anuncio_id = 31,
#                 imovel_id = 33,
#                 plataforma = 'Olx',
#                 taxa_plataforma = '120.0',
#                 criado_em = '2022-6-22',
#                 atualizado_em = '2022-6-22'


# class ReservaTestCase(APITestCase):

#     def setUp(self):
#         self.list_url = reverse('reservas-list')
#         self.reserva_1 = Reserva.objects.create(
#             reserva_id = '2'
#             anuncio_id = '23'
#             check_in = '2022-6-22',
#             check_out = '2022-6-23',
#             preco_total = '250.0'
#             comentarios = 'Teste'
#             numero_hospedes = '12'
#             criado_em = '2022-6-22',
#             atualizado_em = '2022-6-22'

#         )
#         self.reserva_1 = Reserva.objects.create(
#             reserva_id = '1'
#             anuncio_id = '24'
#             check_in = '2022-6-24',
#             check_out = '2022-6-25',
#             preco_total ='300'
#             comentarios = 'Teste 2'
#             numero_hospedes = '6'
#             criado_em = '2022-6-22',
#             atualizado_em = '2022-6-22'

#         )
    
#     def test_requisicao_get_para_listar_reservas(self):
#         """Teste verificador de requisição GET para listar os imoveis """
#         response = self.client.get(self.list_url)
#         self.assertEquals(response.status_code, status.HTTP_200_OK)