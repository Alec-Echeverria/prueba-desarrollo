# Importa la función path para definir las URL patterns
from django.urls import path

# Importa las vistas definidas previamente
from . import views

# Define las URL patterns
urlpatterns = [
    # URL pattern para listar y crear objetos Predio
    path('predios/', views.PredioListCreateView.as_view(), name='predio-list-create'),
    # URL pattern para ver, actualizar y eliminar un objeto Predio específico
    path('predios/<int:pk>/', views.PredioRetrieveUpdateDeleteView.as_view(), name='predio-detail'),
    # URL pattern para listar y crear objetos Propietario
    path('propietarios/', views.PropietarioListCreateView.as_view(), name='propietario-list-create'),
    # URL pattern para ver, actualizar y eliminar un objeto Propietario específico
    path('propietarios/<int:pk>/', views.PropietarioRetrieveUpdateDeleteView.as_view(), name='propietario-detail'),
]
