from django.test import TestCase
from .models import Parking, Car
from datetime import datetime

class ParkingTestCase(TestCase):

    def test_parking_set_up(self):
        now = datetime.today()
        plate = Car.objects.create(plate='FAA-1234')
        parking = Parking.objects.create(plate=plate)
        self.assertEqual(parking.time, '0 minutos')
        self.assertIs(parking.paid, False)
        self.assertIs(parking.left, False)
        self.assertIs(parking.entrada.day, now.day)
        self.assertIs(parking.entrada.hour, now.hour)
        self.assertIs(parking.entrada.minute, now.minute)
        self.assertIs(parking.saida, None)

    def test_car_cant_left_if_not_pay(self):
        plate = Car.objects.create(plate='FAA-1234')
        parking = Parking.objects.create(plate=plate)
        parking.left = True
        parking.save()
        self.assertIs(parking.left, False)

    def test_if_car_left_set_saida(self):
        now = datetime.today()
        plate = Car.objects.create(plate='FAA-1234')
        parking = Parking.objects.create(plate=plate)
        parking.paid = True
        parking.left = True
        parking.save()
        self.assertIs(parking.saida.day, now.day)
        self.assertIs(parking.saida.hour, now.hour)
        self.assertIs(parking.saida.minute, now.minute)
