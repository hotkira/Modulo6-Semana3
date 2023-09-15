from django.shortcuts import render
from base.forms import ContatoForm
from base.forms import ReservaDeBanhoForm
from base.models import Contato

# Create your views here.
def inicio(request):
  return render(request, 'inicio.html')


def contato(request):
  print('método: ',request.method)
  sucesso = False

  form = ContatoForm(request.POST or None)
  if form.is_valid():
    form.save()
    sucesso = True

  context = {
    "nome": "Humberto Kira",
    "telefone": "81 99999999",
    "form": form,
    "sucesso": sucesso
  }
  return render(request, 'contato.html', context)

def reservaDeBanho(request):
  sucesso = False

  form = ReservaDeBanhoForm(request.POST or None)
  if form.is_valid():
    form.save()
    sucesso = True

  context = {
    "form": form,
    "sucesso": sucesso
  }

  return render(request, 'reserva_de_banho.html', context)