from django.contrib import admin
from appHEM.models import Medico
from appHEM.models import Paciente
from appHEM.models import Favoritos
from appHEM.models import Mensagem

# Register your models here.
admin.site.register(Medico)
admin.site.register(Paciente)
admin.site.register(Favoritos)
admin.site.register(Mensagem)
