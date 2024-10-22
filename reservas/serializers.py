from rest_framework import serializers
from .models import Servidor, Horario, Espaco, Reserva, ReservaHorario

class ServidorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servidor
        fields = ['matricula', 'nome', 'funcao', 'ativo', 'email', 'ult_acesso']

class HorarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Horario
        fields = ['id', 'numero_aula', 'horario']

class EspacoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Espaco
        fields = ['id', 'nome', 'ativo']

class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = ['id', 'matricula', 'espaco', 'data', 'motivo', 'turma', 'data_hora_reserva']

class ReservaHorarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReservaHorario
        fields = ['reserva', 'numero_aula']
