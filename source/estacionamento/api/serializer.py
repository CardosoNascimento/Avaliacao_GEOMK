from rest_framework import serializers
from ..models import *

class EstacionamentoSerializer(serializers.ModelSerializer):

    
    class Meta:
        model = Estacionamento
        fields = '__all__'