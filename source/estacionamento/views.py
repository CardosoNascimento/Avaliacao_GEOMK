from rest_framework.response import Response
from rest_framework import viewsets
from .models import Estacionamento
from .serializers import EstacionamentoSerializer
from django.shortcuts import get_object_or_404


class EstacionamentoView(viewsets.ModelViewSet):
    serializer_class = EstacionamentoSerializer

    def get_queryset(self):
        return Estacionamento.objects.all()
