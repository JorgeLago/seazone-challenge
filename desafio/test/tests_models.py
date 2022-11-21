from rest_framework.test import APITestCase
from desafio.models import Imovel, Reserva, Anuncio
from django.urls import reverse
from rest_framework import status

class ImovelTestCase(APITestCase):

    def setUp(self):
        self.list_url = reverse('imoveis-list')
        self.imovel_1 = Imovel.objects.create(
            id_imovel = '3333',
            limite_hospedes = '12',
            banheiros = '3',
            pet_friendly = 'S',
            valor_limpeza = '120.0',
            data_ativacao = '21/06/22',
            criado_em = '21/06/22',
            atualizado_em = '21/06/22'
        )
        self.imovel_2 = Imovel.objects.create(
            id_imovel = '2234',
            limite_hospedes = '13',
            banheiros = '5',
            pet_friendly = 'N',
            valor_limpeza = '120.0',
            data_ativacao = '22/06/22',
            criado_em = '22/06/22',
            atualizado_em = '22/06/22'
        )

    #def test_falhou(self):
        #self.fail('De propósito')
    def test_requisicao_get_para_listar_imoveis(self):
        """Teste verificador de requisição GET para listar os imoveis """
        response = self.client.get(self, list_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)