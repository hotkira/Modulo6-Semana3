from django.db import models

# Create your models here.
class ReservaDeBanho(models.Model):
  TAMANHO_OPCOES = (
    (0, 'Pequeno'),
    (1, 'Médio'),
    (2, 'Grande')
  )
  TURNO_OPCOES = (
    ('manha', 'Manhã'),
    ('tarde', 'Tarde')
  )
  nomeDoPet = models.CharField(verbose_name='Nome do PET', max_length=50)
  telefone = models.CharField(verbose_name='Telefone', max_length=15)
  email = models.EmailField(verbose_name='E-mail', max_length=75)
  diaDaReserva = models.DateField(verbose_name='Dia da Reserva')
  observacoes = models.TextField(verbose_name='Observações', blank=True)
  turno = models.CharField(verbose_name='Turno', choices=TURNO_OPCOES, max_length=5)
  tamanho = models.IntegerField(verbose_name='Tamanho', choices=TAMANHO_OPCOES)

  class Meta:
    verbose_name = 'Formulário de Reserva de Banho'
    verbose_name_plural = 'Formulários de Reservas de Banhos'
