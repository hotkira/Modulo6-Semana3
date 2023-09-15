from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from reserva.forms import ReservaDeBanhoForm

from reserva.models import ReservaDeBanho

 

def criar_reserva_banho(request):
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