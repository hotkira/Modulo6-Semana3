from rest_framework. serializers import ModelSerializer
from reserva.models import ReservaDeBanho
from base.models import Contato

class AgendamentoModelSerializer(ModelSerializer):
    class Meta:
        model = ReservaDeBanho
        fields = '__all__'
        
class ContatoModelSerializer(ModelSerializer):
    class Meta:
        model = Contato
        fields = '__all__'
        

        
    
