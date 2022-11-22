# API's REST CLIENTE
[![NPM](https://img.shields.io/npm/l/react)](https://github.com/JorgeLago/readme-template/blob/main/LICENSE)

# Sobre o projeto


A aplicação consiste em ter 3 API's REST.

Na qual a empresa cliente precisa de um novo sistema para criar um banco de dados com 3 entidades: Imóveis, Anúncios e Reservas. Um imóvel pode ter diversos anúncios, mas um anúncio é referente apenas a um imóvel. Um anúncio pode ter várias reservas, mas uma reserva se refere a apenas um anúncio.

## Parâmetros de Criação de Entidades:

A tabela de imóveis deve conter: o código do imóvel, o limite de hóspedes, a quantidade de banheiros, se aceita animais de estimação, o valor de limpeza, a data de ativação, a data e horário de criação e a data e horaŕio de atualização.

A tabela de anúncios deve conter: a qual imóvel o anúncio pertence, nome da plataforma em que o anúncio foi publicado (ex: AirBnb) , a taxa da plataforma, a data e horário de criação e a data e horário de atualização.

A tabela de reservas deve conter: o código da reserva (gerado aleatoriamente), a qual anúncio a reserva pertence, data de check-in, data de check-out, preço total, campo de comentário, número de hóspedes, data e horário de criação e data e horário de atualização.

Datas e horários de criação e de atualização devem ser inseridos automaticamente no sistema, e não manualmente.

## É possível se fazer com essas API's:
API1 - Referente a Imovéis: É possível buscar uma lista de imóveis, buscar um imóvel individual, criar, alterar e deletar um imóvel;

API 2 - Referente a Anúncios: É possível buscar uma lista de anúncios, buscar um anúncio individual, criar um anúncio e alterar um anúncio, mas não apagá-lo;

API 3 - Referente a Reservas: É possível buscar uma lista de reservas, buscar uma reserva individual, criar uma reserva e deletar uma reserva, mas não alterá-la;

## Layout web
![image](https://user-images.githubusercontent.com/110360494/203220866-e55f91fe-5ff4-451e-8582-ddac9ef54b61.png)

# Layout Criação Imóvel:
![image](https://user-images.githubusercontent.com/110360494/203221109-a193ee8c-b961-4565-974f-edf15c210eb2.png)


# Layout Criação Anúncios:
![image](https://user-images.githubusercontent.com/110360494/203221305-bdee13ae-58a3-4568-912a-36fc61df2135.png)


# Layout Criação Reservas:
![image](https://user-images.githubusercontent.com/110360494/203221374-2ae907fa-3e07-4bea-91f3-60c5f7bd7f4f.png)


# Apps Instalados:
![image](https://user-images.githubusercontent.com/110360494/203219651-c628c443-45c1-4594-80ae-27848d54019e.png)

# Rotas Cadastradas:
![image](https://user-images.githubusercontent.com/110360494/203219819-3db040ce-0b89-43cc-b4a0-142b79e452ab.png)




# Tecnologias utilizadas
## Back end
- Python
- Django
- Django Rest Framework

## Implantação em produção

- Banco de dados: ORM do Django

# Como executar o projeto
- Para executar o projeto, é necessário ter instalado as tecnologias acima citadas.
- Ao clonar o repositório, percebe-se que no banco de dados 'db.sqlite3' já possui dados para testes com as 3 API's.
- No terminal, dê o comando ( python manage.py runserver ) e espere gerar o link para localhost, para acessar a aplicação web.
- Possui autenticação básica, na qual o admin : seazone e a senha : sea1234 .

## Banco de Dados Previamente Populado para testes:
![image](https://user-images.githubusercontent.com/110360494/203219995-79aaa2b0-02f7-4e32-8805-e037f5d150f7.png)


## Back end
Pré-requisitos: Python3 e Django RestFramework


# executar o projeto
python manage.py runserver
```

```bash
# clonar repositório
git clone gh repo clone JorgeLago/seazone-challenge



# Autor

Jorge Luis Silva do Lago

https://www.linkedin.com/in/jorgelslago

