from django.urls import path

from .views import *


app_name = "parking"


urlpatterns = [
    path('', APIView.as_view()),
    path('parking/', ParkingView.as_view()),
    path('parking/<int:pk>/', SingleParkingView.as_view()),
    path('parking/<int:pk>/pay/', PagarView.as_view()),
    path('parking/<int:pk>/out/', SairView.as_view()),
    path('parking/plate/', PlateView.as_view()),
    path('parking/plate/<int:pk>/', HistoricoView.as_view()),
]
