from django.contrib import admin
from .models import *


@admin.register(Estacionamento)
class EstacionamentoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'placa',
        'tempo',
        'pago',
        'saiu'
    )
    fields = ['placa', 'tempo', 'pago', 'saiu', 'entrada', 'saida']
