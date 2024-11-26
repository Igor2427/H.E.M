from django.contrib import admin
from appHEM.models import Medico
from appHEM.models import Paciente
from appHEM.models import Favoritos

# Register your models here.
admin.site.register(Medico)
admin.site.register(Paciente)
admin.site.register(Favoritos)
