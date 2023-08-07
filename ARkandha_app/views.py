# Importa los módulos y clases necesarios de Django REST Framework
from rest_framework import generics, status
from rest_framework.response import Response

# Importa los modelos y los serializadores definidos previamente
from .models import Predio, Propietario, PropietarioPredio
from .serializer import PredioSerializer, PropietarioSerializer, PropietarioPredioSerializer

# Define una vista basada en clase para listar y crear objetos Predio
class PredioListCreateView(generics.ListCreateAPIView):
    queryset = Predio.objects.all()
    serializer_class = PredioSerializer

# Define una vista basada en clase para ver, actualizar y eliminar objetos Predio
class PredioRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Predio.objects.all()
    serializer_class = PredioSerializer

# Define una vista basada en clase para listar y crear objetos Propietario
class PropietarioListCreateView(generics.ListCreateAPIView):
    queryset = Propietario.objects.all()
    serializer_class = PropietarioSerializer

    # Sobrescribe el método create para asociar un predio si se proporciona predio_pk en la solicitud
    def create(self, request, *args, **kwargs):
        predio_pk = request.data.get('predio_pk')
        if predio_pk:
            try:
                predio = Predio.objects.get(pk=predio_pk)
                request.data['predios'] = [predio.pk]
            except Predio.DoesNotExist:
                pass

        return super().create(request, *args, **kwargs)

# Define una vista basada en clase para ver, actualizar y eliminar objetos Propietario
class PropietarioRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Propietario.objects.all()
    serializer_class = PropietarioSerializer

# Define una vista basada en clase para eliminar objetos PropietarioPredio
class PropietarioPredioDestroyView(generics.DestroyAPIView):
    queryset = PropietarioPredio.objects.all()
    serializer_class = PropietarioPredioSerializer

    # Sobrescribe el método destroy para retornar una respuesta con estado HTTP 204 NO CONTENT
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

# Define una vista basada en clase para listar y crear objetos PropietarioPredio asociados a un Predio específico
class PropietarioPredioListCreateView(generics.ListCreateAPIView):
    queryset = PropietarioPredio.objects.all()
    serializer_class = PropietarioPredioSerializer

    # Sobrescribe el método get_queryset para filtrar los objetos PropietarioPredio por predio_pk
    def get_queryset(self):
        pk = self.kwargs.get('pk')
        return PropietarioPredio.objects.filter(predio=pk)

    # Sobrescribe el método perform_create para asociar el Predio correspondiente al objeto PropietarioPredio creado
    def perform_create(self, serializer):
        predio_pk = self.kwargs.get('pk')
        predio = Predio.objects.get(pk=predio_pk)
        serializer.save(predio=predio)
