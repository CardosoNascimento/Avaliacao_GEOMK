from django.contrib import admin
from .models import *

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    pass


@admin.register(Parking)
class parkingAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'plate',
        'time',
        'paid',
        'left'
    )
    fields = ['plate', 'time', 'paid', 'left', 'entrada', 'saida']
