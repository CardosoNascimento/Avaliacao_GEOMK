from django.urls import path
from .views import EstacionamentoView

app_name = 'estacionamento'

urlpatterns = [
    path('estacionamento/', EstacionamentoView.as_view()),
]