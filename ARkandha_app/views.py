from rest_framework import generics, status
from rest_framework.response import Response
from .models import Predio, Propietario, PropietarioPredio
from .serializer import PredioSerializer, PropietarioSerializer, PropietarioPredioSerializer

class PredioListCreateView(generics.ListCreateAPIView):
    queryset = Predio.objects.all()
    serializer_class = PredioSerializer

class PredioRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Predio.objects.all()
    serializer_class = PredioSerializer

class PropietarioListCreateView(generics.ListCreateAPIView):
    queryset = Propietario.objects.all()
    serializer_class = PropietarioSerializer

    def create(self, request, *args, **kwargs):
        predio_pk = request.data.get('predio_pk')
        if predio_pk:
            try:
                predio = Predio.objects.get(pk=predio_pk)
                request.data['predios'] = [predio.pk]
            except Predio.DoesNotExist:
                pass

        return super().create(request, *args, **kwargs)

class PropietarioRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Propietario.objects.all()
    serializer_class = PropietarioSerializer

class PropietarioPredioDestroyView(generics.DestroyAPIView):
    queryset = PropietarioPredio.objects.all()
    serializer_class = PropietarioPredioSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

class PropietarioPredioListCreateView(generics.ListCreateAPIView):
    queryset = PropietarioPredio.objects.all()
    serializer_class = PropietarioPredioSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        return PropietarioPredio.objects.filter(predio=pk)

    def perform_create(self, serializer):
        predio_pk = self.kwargs.get('pk')
        predio = Predio.objects.get(pk=predio_pk)
        serializer.save(predio=predio)
