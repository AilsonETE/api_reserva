from django.contrib import admin
from .models import Servidor, Horario, Espaco, Reserva, ReservaHorario


admin.site.register(Servidor)
admin.site.register(Horario)
admin.site.register(Espaco)
admin.site.register(Reserva)
admin.site.register(ReservaHorario)
