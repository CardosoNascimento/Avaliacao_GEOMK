from django.db import models
from datetime import datetime
from cardosoteste.validators import *


class Carro(models.Model):
    placa = models.CharField(max_length=8, validators=[placa_validator])
    
    def __str__(self):
        return f'{self.placa}'

    def save(self, *args, **kwargs):
        self.placa = str(self.placa).upper()
        super(Carro, self).save(*args, **kwargs)

         
class Estacionamento(models.Model):
    placa = models.ForeignKey(Carro, on_delete=models.CASCADE)
    tempo = models.CharField(max_length=30, default='0 minutos')
    pago = models.BooleanField(default=False)
    saiu = models.BooleanField(default=False)
    entrada = models.DateTimeField(default=datetime.today())
    saida = models.DateTimeField(null=True, blank=True)

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
        if self.saiu and self.saida == None:
            self.saida = datetime.today()
            horas = int(self.saida.hour) - int(self.entrada.hour)
            minutos = int(self.saida.minute) - int(self.entrada.minute)
            tempo = ''
            if horas == 0:
                tempo = '{} minuto{}'.format(minutos, '' if minutos == 1 else 's')
            else:
                tempo = '{} hora{} e {} minutos'.format(horas, '' if horas == 1 else 's', minutos)
            self.tempo = tempo
        else:
            horas = int(agr.hour) - int(self.entrada.hour)
            minutos = int(agr.minute) - int(self.entrada.minute)
            tempo = ''
            if horas == 0:
                tempo = '{} minuto{}'.format(minutos, '' if minutos == 1 else 's')
            else:
                tempo = '{} hora{} e {} minutos'.format(horas, '' if horas == 1 else 's', minutos)
            self.tempo = tempo
        super(Estacionamento, self).save(*args, **kwargs)
