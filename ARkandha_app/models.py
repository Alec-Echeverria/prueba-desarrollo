from django.db import models

class Propietario(models.Model):
    # Definición de opciones para el campo 'tipo_identificacion'
    TIPO_IDENTIFICACION_CHOICES = [
        ('CC', 'Cédula de ciudadanía'),
        ('CE', 'Cédula de extranjería'),
        ('NIT', 'Número de identificación tributaria'),
        ('TI', 'Tarjeta de Identidad'),
    ]

    # Atributos del modelo Propietario
    nombre = models.CharField(max_length=100, null=False, blank=False)
    tipo_identificacion = models.CharField(max_length=3, choices=TIPO_IDENTIFICACION_CHOICES, null=False, blank=False)
    numero_identificacion = models.BigIntegerField(primary_key=True)  # Usar la cédula como clave primaria
    tipo = models.CharField(max_length=10, choices=[('N', 'Natural'), ('J', 'Jurídico')], null=False, blank=False)
    predios = models.ManyToManyField('Predio', blank=True)  # Relación muchos a muchos con el modelo Predio

    def __str__(self):
        return f"{self.nombre} - Cédula: {self.numero_identificacion}"

class Predio(models.Model):
    # Definición de opciones para el campo 'tipo'
    TIPO_PREDIO_CHOICES = [
        ('U', 'Urbano'),
        ('R', 'Rural'),
    ]

    # Atributos del modelo Predio
    direccion = models.CharField(max_length=200)
    tipo = models.CharField(max_length=1, choices=TIPO_PREDIO_CHOICES)
    numero_catastral = models.BigIntegerField(primary_key=True)  # Usar el número de catastro como clave primaria
    numero_matricula = models.CharField(max_length=30, unique=True)
    propietarios = models.ManyToManyField('Propietario', blank=True)  # Relación muchos a muchos con el modelo Propietario

    def __str__(self):
        return f"Número Catastral: {self.numero_catastral}"

class PropietarioPredio(models.Model):
    # Atributos del modelo PropietarioPredio
    propietario = models.ForeignKey(Propietario, on_delete=models.CASCADE)  # Relación muchos a uno con el modelo Propietario
    predio = models.ForeignKey(Predio, on_delete=models.CASCADE)  # Relación muchos a uno con el modelo Predio

    def __str__(self):
        return f"{self.propietario} - {self.predio}"
