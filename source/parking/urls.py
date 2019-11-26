from django.urls import path

from .views import *


app_name = "parking"


urlpatterns = [
    path('parking/', ParkingView.as_view()),
    path('parking/<int:pk>/', HistoricoView.as_view()),
    path('parking/<int:pk>/out/', SairView.as_view()),
    path('parking/<int:pk>/pay/', PagarView.as_view()),
]