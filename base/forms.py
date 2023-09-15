from django import forms
from base.models import Contato
from base.models import ReservaDeBanho

class ContatoForm(forms.ModelForm):
  class Meta:
    model = Contato
    fields = ['nome', 'email', 'mensagem']

class ReservaDeBanhoForm(forms.ModelForm):
  class Meta:
    model = ReservaDeBanho
    fields = ['nomeDoPet', 'telefone', 'diaDaReserva', 'observacoes']
    # labels = {
    #   'nomeDoPet': 'Nome do PET',
    #   'diaDaReserva': 'Dia da reserva',
    #   'observacoes': 'Observações'
    # }
    widgets = {
      'diaDaReserva': forms.DateInput(attrs={'type': 'date'}),
    }
  