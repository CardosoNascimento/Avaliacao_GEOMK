from rest_framework import serializers
from .serializers import EstacionamentoSerializer
from .models import *

class EstacionamentoSerializer(serializers.ModelSerializer):


    class Meta:
        model = Estacionamento
        fields = '__all__'
