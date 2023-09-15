from typing import Any
from django.core.management.base import BaseCommand
from model_bakery import baker

from reserva.models import ReservaDeBanho

class Command(BaseCommand):
    help = 'Criar dados fakes para testar a API agendamento'
    
    def handle(self, *args, **options):
        total = 50
        self.stdout .write(
            self.style.WARNING(f'Criando {total} agendamentos')
        )
        for i in range(total):
            reserva = baker.make(ReservaDeBanho)
            reserva.save()

        self.stdout.write(
            self.style.SUCCESS('Agendamentos criados')
        )