from django.shortcuts import render
#primeiro
#import json
from django.http import HttpResponse
from datetime import date, datetime
from base.models import Contato
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
#from base.models import ReservaDeBanho
from reserva.models import ReservaDeBanho
from rest_framework import status
from rest_framework. viewsets import ModelViewSet
from rest_framework import viewsets
from rest_api.serializers import AgendamentoModelSerializer, ContatoModelSerializer
from rest_framework.authentication import TokenAuthentication
#from rest_framework.permissions import IsAuthenticated
#IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly
# Create your views here.
class AgendamentoModelViewSet(ModelViewSet):
    queryset = ReservaDeBanho.objects.all()
    serializer_class = AgendamentoModelSerializer
    authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]
    permission_classes =[IsAuthenticatedOrReadOnly]
    

class ContatoModelViewSet(ModelViewSet):
    queryset = Contato.objects.all()
    serializer_class = ContatoModelSerializer
    
   #mostra apenas os contatos que não foram lidos 
class ContatoNaoLidoModelViewSet(ModelViewSet):
    queryset = Contato.objects.filter(lido=False)
    serializer_class = ContatoModelSerializer
    
class AgendamentoNomeModelViewSet(viewsets.ModelViewSet):
    serializer_class = AgendamentoModelSerializer

    def get_queryset(self):
        # Filtra os registros em que o nomeDoPet começa com "A"
        return ReservaDeBanho.objects.filter(nomeDoPet__istartswith='A')

class AgendamentoObservacoesBrancoModelViewSet(ModelViewSet):
    # Filtra os registros com observacoes em branco
    queryset = ReservaDeBanho.objects.filter(observacoes='')  # Filtra os registros com observacoes em branco
    serializer_class = AgendamentoModelSerializer
    

    
# opção 2 
@api_view(['GET', 'POST'])
def reservadebanho(request):
    consulta = ReservaDeBanho.objects.all()
    dados = []
    
    for reservadebanho in consulta:
        dado = {
            'id': reservadebanho.id,
            'nomeDoPet': reservadebanho.nomeDoPet,
            'telefone': reservadebanho.telefone,
            'email': reservadebanho.email,
            'dia_da_reserva': reservadebanho.diaDaReserva,  # Converte a data em string
            'observacoes': reservadebanho.observacoes,
            'turno':reservadebanho.turno,
            'tamanho':reservadebanho.tamanho,
        }
        dados.append(dado)
    

    return Response(dados)
 
#exemplo se tivesse chave estrangeira  
# @api_view(['GET', 'POST'])
# def ver_banho(request):
#     consulta = ReservaDeBanho.objects.all()
#     dados = []
#     for banho in consulta:
#       dado ={
#       'id': banho.id,
#       'nomeDoPet': banho.nomeDoPet,
#       'categoria':{
  #campos da tabela estrangeira
  #         },  'email': banho.email, por exemplo
  #
#       }
#       'telefone': banho.telefone,
#       'email': banho.email,
#       'diaDaReserva': banho.diaDaReserva,
#       'observacoes': banho.observacoes,
#       'turno':banho.turno,
#       'tamanho':banho.tamanho,      
        
#       }

#função dias para o fim do ano

from datetime import date

@api_view(http_method_names=['GET'])
def dias_reserva_banho_ate_fim_do_ano(request):
    # pega a data atual
    data_atual = date.today()

    # pega todos os registros de ReservaDeBanho
    banhos = ReservaDeBanho.objects.all()

    # lista de dicionários com os dados de cada reserva e dias restantes para o final do ano
    dados = []
    for banho in banhos:
        data_reserva = banho.diaDaReserva

        # quantos dias faltam para o final do ano a partir da data da reserva
        dias_para_fim_do_ano = (date(data_reserva.year, 12, 31) - data_reserva).days

        dado = {
            'id': banho.id,
            'nomeDoPet': banho.nomeDoPet,
            'diaDaReserva': banho.diaDaReserva.strftime('%Y-%m-%d'),
            'dias_para_fim_do_ano': dias_para_fim_do_ano,
        }
        dados.append(dado)

    return Response(dados)

#API que calcula a quantidade de letras do nome do pet
@api_view(http_method_names=['GET'])
def quantidade_de_letras_pet(request):
    # pega todos os registros de ReservaDeBanho
    banhos = ReservaDeBanho.objects.all()

    # lista de dicionários com os dados de cada reserva e a quantidade de letras no nomeDoPet
    dados = []
    for banho in banhos:
        # pega a quantidade de letras no nomeDoPet
        quantidade_de_letras = len(banho.nomeDoPet)

        dado = {
            'id': banho.id,
            'nomeDoPet': banho.nomeDoPet,
            'quantidade_de_letras': quantidade_de_letras,
        }
        dados.append(dado)

    return Response(dados)


#função para adicionar
@api_view(http_method_names=['POST'])
def adicionar_banho(request):
  nomeDoPet = request.data['nomeDoPet']
  telefone = request.data['telefone']
  email = request.data['email']
  diaDaReserva = request.data['diaDaReserva']
  observacoes = request.data.get('observacoes', '')
  turno = request.data['turno']
  tamanho = request.data['tamanho']
  banho = ReservaDeBanho.objects.create(nomeDoPet=nomeDoPet, telefone=telefone, email=email, diaDaReserva=diaDaReserva, observacoes=observacoes, turno=turno, tamanho=tamanho)
  dado = {
      'id': banho.id,
      'nomeDoPet': banho.nomeDoPet,
      'telefone': banho.telefone,
      'email': banho.email,
      'diaDaReserva': banho.diaDaReserva,
      'observacoes': banho.observacoes,
      'turno':banho.turno,
      'tamanho':banho.tamanho,
  }
  return Response(dado)
  
  
  
#opção 1 fazendo o json
# def reservadebanho(request):
#     consulta = ReservaDeBanho.objects.all()
#     dados = []
    
#     for reservadebanho in consulta:
#         dado = {
#             'id': reservadebanho.id,
#             'nome': reservadebanho.nomeDoPet,
#             'dia_da_reserva': reservadebanho.diaDaReserva.strftime('%Y-%m-%d'),  # Converte a data em string
#         }
#         dados.append(dado)
    
#     # Converte a lista de dados em JSON
#     dados_json = json.dumps(dados)
    
#     # Cria uma HttpResponse com o JSON como conteúdo
#     response = HttpResponse(dados_json, content_type='application/json')
    
#     return response
    

  
# Create your views here.
@api_view(['GET', 'POST'])
def hello_world(request):
  if request.method == 'POST':
    nome = request.data.get('nome')
    return Response({ "mensagem": f'Olá, {nome}!!' })

  return Response({ 'Hello': 'hello world!' })


@api_view(['GET'])
def listar_contatos(request):
  contatos = Contato.objects.all().order_by('nome')
  contatosFormatados = []

  for contato in contatos:
    contatosFormatados.append({ 
      "nome": contato.nome, 
      "email": contato.email,
      "id": contato.id
    })

  return Response({ 'contatos': contatosFormatados })


@api_view(['GET', 'PUT'])
def obter_contato_pelo_id(request, id):
  contato = Contato.objects.filter(id=id)

  if len(contato) == 0:
    return Response({ "mensagem": "Não foi encontrado nenhum contato com esse ID." })
  
  if request.method == 'PUT':
    nome = request.data.get('nome')
    email = request.data.get('email')
    mensagem = request.data.get('mensagem')

    contato[0].nome = nome
    contato[0].email = email
    contato[0].mensagem = mensagem

    contato[0].save()

    return Response({ "contato": "contato atualizado" })

  contatoFormatado = {
    "nome": contato[0].nome,
    "email": contato[0].email,
    "mensagem": contato[0].mensagem,
    "id": contato[0].id
  }

  return Response({ "contato": contatoFormatado })


