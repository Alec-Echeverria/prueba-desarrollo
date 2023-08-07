from django.contrib import admin
from .models import Predio, Propietario, PropietarioPredio

# Definir un Inline para la relación ManyToMany entre Propietario y Predio a través de la tabla intermedia PropietarioPredio
class PropietarioPredioInline(admin.TabularInline):
    model = PropietarioPredio

@admin.register(Predio)
class PredioAdmin(admin.ModelAdmin):
    inlines = [PropietarioPredioInline]
    raw_id_fields = ['propietarios']

@admin.register(Propietario)
class PropietarioAdmin(admin.ModelAdmin):
    inlines = [PropietarioPredioInline]
    raw_id_fields = ['predios']
