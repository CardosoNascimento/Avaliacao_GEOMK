# from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import viewsets
from rest_framework.views import APIView
from .models import *
from .serializers import ParkingSerializer, HistoricoSerializer
from rest_framework.response import Response
from rest_framework import status


class ParkingView(APIView):

    def get(self, request):
        parking = Parking.objects.all()
        serializer = ParkingSerializer(parking, many=True)
        return Response({"parking": serializer.data})

    def post(self, request, format=None):
        serializer = ParkingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HistoricoView(APIView):

    def get(self, request, pk):
        placa = Car.objects.get(id=pk)
        parking = Parking.objects.filter(plate=placa)
        serializer = HistoricoSerializer(parking, many=True)
        return Response({"Histórico da placa '{}'".format(placa.plate): serializer.data})


class SairView(APIView):

    def get(self, request, pk):
        parking = list(Parking.objects.filter(id=pk))[0]
        parking.left = True
        if parking.left and not parking.paid:
            return Response({"Invalido": "'{}' não pagou".format(parking.plate)})
        else:
            parking.left = True
            parking.save()
            serializer = ParkingSerializer(parking, many=False)
            return Response({"{} saiu".format(parking.plate): serializer.data})

    
class PagarView(APIView):

    def get(self, request, pk):
        parking = list(Parking.objects.filter(id=pk))[0]    
        parking.paid = True
        parking.save()
        serializer = ParkingSerializer(parking, many=False)
        return Response({"Pago": serializer.data})
