from rest_framework import viewsets
from ..models import *
from .serializer import *

class EstacionamentoViewSet(viewsets.ModelViewSet):
    serializer_class = EstacionamentoSerializer

    def get_queryset(self):
        return Estacionamento.objects.all()