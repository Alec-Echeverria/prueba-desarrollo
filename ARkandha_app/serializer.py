# Importa el módulo serializers de Django REST Framework
from rest_framework import serializers

# Importa los modelos que serán utilizados en el serializador
from .models import Predio, Propietario, PropietarioPredio

# Define el serializador PropietarioSerializer
class PropietarioSerializer(serializers.ModelSerializer):
    # Define el campo "predios" como un PrimaryKeyRelatedField
    # que permite asociar múltiples objetos Predio a un objeto Propietario
    predios = serializers.PrimaryKeyRelatedField(queryset=Predio.objects.all(), many=True)

    # Define la clase Meta para proporcionar metadatos al serializador
    class Meta:
        # Especifica el modelo a utilizar para la serialización (Propietario)
        model = Propietario
        # Especifica los campos del modelo a incluir en la serialización
        fields = ['nombre', 'tipo_identificacion', 'numero_identificacion', 'tipo', 'predios']

    # Sobrescribe el método create para manejar la creación de un nuevo objeto Propietario
    def create(self, validated_data):
        # Extrae los datos relacionados con los predios del objeto validado
        predios_data = validated_data.pop('predios', [])
        
        # Crea el objeto Propietario con los datos validados (excluyendo predios_data)
        propietario = Propietario.objects.create(**validated_data)

        # Itera a través de los predios_data y crea objetos PropietarioPredio
        # para asociar los predios seleccionados con el Propietario creado
        for predio in predios_data:
            PropietarioPredio.objects.create(propietario=propietario, predio=predio)

        # Retorna el objeto Propietario recién creado
        return propietario

# Define el serializador PropietarioPredioSerializer
class PropietarioPredioSerializer(serializers.ModelSerializer):
    # Define el campo "propietario" utilizando el serializador PropietarioSerializer
    # Esto permitirá incluir los detalles del Propietario en la serialización de PropietarioPredio
    propietario = PropietarioSerializer()

    # Define la clase Meta para proporcionar metadatos al serializador
    class Meta:
        # Especifica el modelo a utilizar para la serialización (PropietarioPredio)
        model = PropietarioPredio
        # Especifica los campos del modelo a incluir en la serialización
        fields = ('propietario',)

    # Sobrescribe el método create para manejar la creación de un nuevo objeto PropietarioPredio
    def create(self, validated_data):
        # Eliminamos el campo "predio" del diccionario validado para evitar que se asocie automáticamente
        predio = validated_data.pop('predio', None)
        # Llamamos al método create de la superclase para crear el objeto PropietarioPredio
        instance = super().create(validated_data)
        # Si se proporcionó el campo "predio", lo asociamos manualmente al objeto PropietarioPredio
        if predio:
            instance.predio = predio
            instance.save()
        # Retorna el objeto PropietarioPredio recién creado
        return instance

# Define el serializador PredioSerializer
class PredioSerializer(serializers.ModelSerializer):
    # Define el campo "propietarios" utilizando el serializador PropietarioPredioSerializer
    # Esto permitirá incluir los detalles de los PropietarioPredio asociados al Predio en la serialización
    propietarios = PropietarioPredioSerializer(many=True, read_only=True, source='propietariopredio_set')

    # Define la clase Meta para proporcionar metadatos al serializador
    class Meta:
        # Especifica el modelo a utilizar para la serialización (Predio)
        model = Predio
        # Especifica todos los campos del modelo para incluirlos en la serialización
        fields = '__all__'
