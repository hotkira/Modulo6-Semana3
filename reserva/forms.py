from django import forms
from datetime import date

from reserva.models import ReservaDeBanho

class ReservaDeBanhoForm(forms.ModelForm):
  class Meta:
    model = ReservaDeBanho
    fields = ['nomeDoPet', 'telefone', 'email', 'diaDaReserva', 'turno', 'tamanho', 'observacoes']
    widgets = {
      'diaDaReserva': forms.DateInput(attrs={'type': 'date'}),
    }
  
  def clean_diaDaReserva(self):
    print('inicio da validacao customizada')
    diaDaReservaSelecionado = self.cleaned_data['diaDaReserva']
    hoje = date.today()
  
    if diaDaReservaSelecionado < hoje:
      raise forms.ValidationError('Não é possível reservar para uma data no passado.')
    
    
    quantidadeDeReservasParaODiaSelecionado = ReservaDeBanho.objects.filter(diaDaReserva=diaDaReservaSelecionado).count()
    print(f'quantidade de reservas para o dia: {quantidadeDeReservasParaODiaSelecionado}')
    if quantidadeDeReservasParaODiaSelecionado >= 4:
      raise forms.ValidationError('O limite máximo de reservas para este dia já foi atingido. Escolha outra data.')

    return diaDaReservaSelecionado