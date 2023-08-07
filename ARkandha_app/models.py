from django.db import models

class Propietario(models.Model):
    TIPO_IDENTIFICACION_CHOICES = [
        ('CC', 'Cédula de ciudadanía'),
        ('CE', 'Cédula de extranjería'),
        ('NIT', 'Número de identificación tributaria'),
        ('TI', 'Tarjeta de Identidad'),
    ]
    nombre = models.CharField(max_length=100, null=False, blank=False)
    tipo_identificacion = models.CharField(max_length=3, choices=TIPO_IDENTIFICACION_CHOICES, null=False, blank=False)
    numero_identificacion = models.BigIntegerField(primary_key=True)  # Usar la cédula como clave primaria
    tipo = models.CharField(max_length=10, choices=[('N', 'Natural'), ('J', 'Jurídico')], null=False, blank=False)
    predios = models.ManyToManyField('Predio', blank=True)

    def __str__(self):
        return f"{self.nombre} - Cédula: {self.numero_identificacion}"

class Predio(models.Model):
    TIPO_PREDIO_CHOICES = [
        ('U', 'Urbano'),
        ('R', 'Rural'),
    ]

    direccion = models.CharField(max_length=200)
    tipo = models.CharField(max_length=1, choices=TIPO_PREDIO_CHOICES)
    numero_catastral = models.BigIntegerField(primary_key=True)  # Usar el número de catastro como clave primaria
    numero_matricula = models.CharField(max_length=30, unique=True)
    propietarios = models.ManyToManyField('Propietario', blank=True)

    def __str__(self):
        return f"Número Catastral: {self.numero_catastral}"

class PropietarioPredio(models.Model):
    propietario = models.ForeignKey(Propietario, on_delete=models.CASCADE)
    predio = models.ForeignKey(Predio, on_delete=models.CASCADE)

    # Otros campos y métodos si los necesitas

    def __str__(self):
        return f"{self.propietario} - {self.predio}"
