from rest_framework import serializers
from .models import Predio, Propietario, PropietarioPredio

class PropietarioSerializer(serializers.ModelSerializer):
    predios = serializers.PrimaryKeyRelatedField(queryset=Predio.objects.all(), many=True)

    class Meta:
        model = Propietario
        fields = ['nombre', 'tipo_identificacion', 'numero_identificacion', 'tipo', 'predios']

    def create(self, validated_data):
        predios_data = validated_data.pop('predios', [])
        propietario = Propietario.objects.create(**validated_data)

        for predio in predios_data:
            PropietarioPredio.objects.create(propietario=propietario, predio=predio)

        return propietario

class PropietarioPredioSerializer(serializers.ModelSerializer):
    propietario = PropietarioSerializer()

    class Meta:
        model = PropietarioPredio
        fields = ('propietario',)

    def create(self, validated_data):
        # Eliminamos el campo "predio" del diccionario validado para que no se asocie automáticamente
        predio = validated_data.pop('predio', None)
        instance = super().create(validated_data)
        if predio:
            instance.predio = predio
            instance.save()
        return instance

class PredioSerializer(serializers.ModelSerializer):
    propietarios = PropietarioPredioSerializer(many=True, read_only=True, source='propietariopredio_set')

    class Meta:
        model = Predio
        fields = '__all__'
