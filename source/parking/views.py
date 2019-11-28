# from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import viewsets
from rest_framework.views import APIView
from .models import *
from .serializers import ParkingSerializer, HistoricoSerializer, PlateSerializer
from rest_framework.response import Response
from rest_framework import status


class APIView(APIView):

    def get(self, request):
        return Response({"http://127.0.0.1:8008/api/parking/, http://127.0.0.1:8008/api/parking/plate/"})


class PlateView(APIView):

    def get(self, request):
        plate = Parking.objects.all()
        serializer = PlateSerializer(plate, many=True)
        return Response({"plate": serializer.data})

    def post(self, request):
        serializer = PlateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Reponse(serializer.data, status=status.HTTP_201_CREATED)        
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class ParkingView(APIView):

    def get(self, request):
        parking = Parking.objects.all()
        serializer = ParkingSerializer(parking, many=True)
        return Response({"parking": serializer.data})

    def post(self, request):
        serializer = ParkingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SingleParkingView(APIView):

    def get(self, request, pk):
        parking = Parking.objects.get(id=pk)
        serializer = ParkingSerializer(parking)
        return Response({"parking": serializer.data})

    def post(self, request, pk):
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
            serializer = ParkingSerializer(parking)
            return Response({"'{}' saiu".format(parking.plate): serializer.data})

    
class PagarView(APIView):

    def get(self, request, pk):
        parking = list(Parking.objects.filter(id=pk))[0]    
        parking.paid = True
        parking.save()
        serializer = ParkingSerializer(parking)
        return Response({"'{}' pago".format(parking.plate): serializer.data})
