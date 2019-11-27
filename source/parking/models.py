from django.db import models
from datetime import datetime
from cardosoteste.validators import *


class Car(models.Model):
    plate = models.CharField(max_length=8, validators=[placa_validator])

    def __str__(self):
        return f'{self.plate}'

    def save(self, *args, **kwargs):
        self.plate = str(self.plate).upper()
        super(Car, self).save(*args, **kwargs)

         
class Parking(models.Model):
    plate = models.ForeignKey(Car, on_delete=models.CASCADE)
    time = models.CharField(max_length=30, default='0 minutos')
    paid = models.BooleanField(default=False)
    left = models.BooleanField(default=False)
    entrada = models.DateTimeField(default=datetime.today())
    saida = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'parking'
    
    def __str__(self): 
        return f'Placa: {self.plate}; Tempo: {self.time}; Pago: {self.paid}; Saiu: {self.left}.'

    def clean(self, *args, **kwargs):
        if self.left and not self.paid:
            raise ValidationError(
                error_messages['saiupagou!']
            )
        super(Parking, self).clean(*args, **kwargs)

    def save(self, *args, **kwargs):
        now = datetime.today()
        if self.left and not self.paid:
            self.left = False
        if self.left and self.saida == None:
            minutos_saida = int(now.hour * 60 + now.minute)
            minutos_entrada = int(self.entrada.hour * 60 + self.entrada.minute)
            minutos_total = minutos_saida - minutos_entrada
            horas = int(minutos_total / 60)
            minutos = minutos_total % 60
            tempo = ''
            if horas == 0:
                tempo = '{} minuto{}'.format(minutos, '' if minutos == 1 else 's')
            else:
                tempo = '{} hora{} e {} minutos'.format(horas, '' if horas == 1 else 's', minutos)
            self.saida = now
            self.time = tempo
        else:
            minutos_saida = int(now.hour * 60 + now.minute)
            minutos_entrada = int(self.entrada.hour * 60 + self.entrada.minute)
            minutos_total = minutos_saida - minutos_entrada
            horas = int(minutos_total / 60)
            minutos = minutos_total % 60
            tempo = ''
            if horas == 0:
                tempo = '{} minuto{}'.format(minutos, '' if minutos == 1 else 's')
            else:
                tempo = '{} hora{} e {} minutos'.format(horas, '' if horas == 1 else 's', minutos)
            self.time = tempo
        super(Parking, self).save(*args, **kwargs)
