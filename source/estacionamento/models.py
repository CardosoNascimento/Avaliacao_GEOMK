from django.db import models
from datetime import datetime
from cardosoteste.validators import *


class Carro(models.Model):
    placa = models.CharField(max_length=8, unique=True, validators=[placa_validator])

    def __str__(self):
        return f'{self.placa}'

    def save(self, *args, **kwargs):
        self.placa = str(self.placa).upper()
        super(Carro, self).save(*args, **kwargs)


class Estacionamento(models.Model):
    placa = models.ForeignKey(Carro, on_delete=models.CASCADE, unique=False)
    tempo = models.CharField(max_length=30, default='0 minutos')
    pago = models.BooleanField(default=False)
    saiu = models.BooleanField(default=False)
    chegada = models.DateTimeField(default=datetime.today())

    class Meta:
        verbose_name_plural = 'Estacionamento'
    
    def __str__(self): 
        return f'Placa: {self.placa}; Tempo: {self.tempo}; Pago: {self.pago}; Saiu: {self.saiu}.'

    def clean(self, *args, **kwargs):
        if self.saiu and not self.pago:
            raise ValidationError(
                error_messages['saiupagou!']
            )
        super(Estacionamento, self).clean(*args, **kwargs)
    def save(self, *args, **kwargs):
        agr = datetime.today()
        anos = int(agr.year) - int(self.chegada.year)
        meses = ((anos*12) + (agr.)

        
