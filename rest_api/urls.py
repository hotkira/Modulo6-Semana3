from django.urls import path

from rest_api.views import *

from rest_framework.routers import SimpleRouter

app_name = 'rest_api'

router = SimpleRouter(trailing_slash=False)
#adicionar prefixo
router.register('agendamento', AgendamentoModelViewSet)
router.register('contato', ContatoModelViewSet)
#estes 3 são da atividade M6S2
router.register('Agendamento_letra_A', AgendamentoNomeModelViewSet, basename='agendamento-data')
router.register('contato_nao_lido', ContatoNaoLidoModelViewSet)
router.register('agendamento_observacoes_branco', AgendamentoObservacoesBrancoModelViewSet)

urlpatterns = [
  path('hello_world', hello_world, name='hello_world_api'),
  #path('contato', listar_contatos, name='listar_contatos'),
  #path('contato/<int:id>', obter_contato_pelo_id, name="obter_contato"),
  path('reservadebanho/', reservadebanho, name='reservadebanho'),
  path('adicionar_banho/', adicionar_banho, name='adicionar_banho'),
  path('quantidade_de_letras_pet/', quantidade_de_letras_pet, name='quantidade_de_letras_pet'),
  path('dias_reserva_banho_ate_fim_do_ano/', dias_reserva_banho_ate_fim_do_ano, name='dias_reserva_banho_ate_fim_do_ano')

]
#urlpatters + routerr.urls
urlpatterns += router.urls

