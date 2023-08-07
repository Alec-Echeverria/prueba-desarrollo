from django.urls import path
from . import views

urlpatterns = [
    path('predios/', views.PredioListCreateView.as_view(), name='predio-list-create'),
    path('predios/<int:pk>/', views.PredioRetrieveUpdateDeleteView.as_view(), name='predio-detail'),
    path('propietarios/', views.PropietarioListCreateView.as_view(), name='propietario-list-create'),
    path('propietarios/<int:pk>/', views.PropietarioRetrieveUpdateDeleteView.as_view(), name='propietario-detail'),
]
