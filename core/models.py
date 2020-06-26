from django.db import models

# Create your models here.
class Delitos(models.Model):
    fecha = models.DateField()
    texto = models.CharField(max_length=400)
    topico = models.CharField(max_length=50)
    latitud = models.FloatField()
    longitud = models.FloatField()
    colonia = models.CharField(max_length=50)
    tipo_delito = models.CharField(max_length=50)
    municipio = models.CharField(max_length=50)

    def __str__(self):
        return self.texto

class DelitoAbierto(models.Model):
    Fecha = models.DateField()
    Municipio = models.CharField(max_length=255)
    Colonia = models.CharField(max_length=255)
    TipoDelito = models.CharField(max_length=255)
    Latitud = models.FloatField()
    Longitud = models.FloatField()

    def __str__(self):
        return self.Municipio

class DelitoNoticia(models.Model):
    Fecha = models.DateField()
    Municipio = models.CharField(max_length=255)
    Colonia = models.CharField(max_length=255)
    TipoDelito = models.CharField(max_length=255)
    Latitud = models.FloatField()
    Longitud = models.FloatField()

class Chart1(models.Model):
    Colonia = models.CharField(max_length=255)
    Delito =  models.CharField(max_length=255)
    Sumatoria = models.IntegerField()
    
class Chart2(models.Model):
    Colonia = models.CharField(max_length=255)
    Delito =  models.CharField(max_length=255)
    Sumatoria = models.IntegerField()

class Chart3(models.Model):
    Muni = models.IntegerField()
    Dia =  models.CharField(max_length=255)
    Total = models.IntegerField()

class Chart4(models.Model):
    Colonia = models.CharField(max_length=255)
    Delito =  models.CharField(max_length=255)
    Sumatoria = models.IntegerField()

class Chart5(models.Model):
    Palabra = models.CharField(max_length=255)
    Conteo = models.IntegerField()

class Chart6(models.Model):
    Municipio = models.CharField(max_length=255)
    Mes =  models.CharField(max_length=255)
    Ano =  models.CharField(max_length=255)
    Sumatoria = models.IntegerField()

