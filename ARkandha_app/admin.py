# Importa la clase admin de Django para configurar el panel de administración
from django.contrib import admin

# Importa los modelos definidos previamente
from .models import Predio, Propietario, PropietarioPredio

# Define un Inline para la relación ManyToMany entre Propietario y Predio a través de la tabla intermedia PropietarioPredio
class PropietarioPredioInline(admin.TabularInline):
    model = PropietarioPredio

# Registra el modelo Predio en el panel de administración y configura la visualización
@admin.register(Predio)
class PredioAdmin(admin.ModelAdmin):
    # Asocia el Inline PropietarioPredioInline para permitir la edición de la relación ManyToMany en línea
    inlines = [PropietarioPredioInline]
    # Utiliza raw_id_fields para mostrar un campo de búsqueda en lugar de una lista desplegable para la relación ManyToMany
    raw_id_fields = ['propietarios']

# Registra el modelo Propietario en el panel de administración y configura la visualización
@admin.register(Propietario)
class PropietarioAdmin(admin.ModelAdmin):
    # Asocia el Inline PropietarioPredioInline para permitir la edición de la relación ManyToMany en línea
    inlines = [PropietarioPredioInline]
    # Utiliza raw_id_fields para mostrar un campo de búsqueda en lugar de una lista desplegable para la relación ManyToMany
    raw_id_fields = ['predios']
