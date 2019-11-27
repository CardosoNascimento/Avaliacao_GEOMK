from rest_framework import serializers
from .models import *


class PlateSerializer(serializers.ModelSerializer):


    class Meta:
        model = Car
        fields = '__all__'

        
class ParkingSerializer(serializers.ModelSerializer):
       

    class Meta:
        model = Parking
        fields = [
            'id',
            'plate',
            'time',
            'paid',
            'left',
            'entrada',
            'saida',
        ]
    


class HistoricoSerializer(serializers.ModelSerializer):


    class Meta:
        model = Parking
        fields = [
            'id',
            'time',
            'paid',
            'left'
        ]
    