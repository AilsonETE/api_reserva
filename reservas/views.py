from rest_framework import viewsets
from .models import Servidor, Horario, Espaco, Reserva, ReservaHorario
from .serializers import (ServidorSerializer, HorarioSerializer, EspacoSerializer,
                          ReservaSerializer, ReservaHorarioSerializer)

class ServidorViewSet(viewsets.ModelViewSet):
    queryset = Servidor.objects.all()
    serializer_class = ServidorSerializer

class HorarioViewSet(viewsets.ModelViewSet):
    queryset = Horario.objects.all()
    serializer_class = HorarioSerializer

class EspacoViewSet(viewsets.ModelViewSet):
    queryset = Espaco.objects.all()
    serializer_class = EspacoSerializer

class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer

class ReservaHorarioViewSet(viewsets.ModelViewSet):
    queryset = ReservaHorario.objects.all()
    serializer_class = ReservaHorarioSerializer
