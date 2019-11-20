from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Estacionamento


class EstacionamentoView(APIView):
    def get(self, request):
        estacionamento = Estacionamento.objects.all()
        return Response({"estacionamento": estacionamento})
        