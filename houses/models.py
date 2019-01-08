from django.db import models

# Create your models here.
class general(models.Model):
    """
    La informacion mas general del inmueble
    """
    direccion = models.CharField(max_length=50)
    ciudad =  models.CharField(max_length = 30)
    departamento = models.CharField(max_length = 30)
    pais = models.CharField(max_length = 30)
    telefono = models.CharField(max_length = 10)

class interior(models.Model):
    """
    Informacion sobre el interior del inmueble
    """
    cuartos = models.IntegerField()
    baños = models.IntegerField()
    closets = models.IntegerField()
    calentador = models.BooleanField(null = True, blank = True)

class exterior(models.Model):
    """
    Informacion del lugar (o sus alrededores) en donde esta situado el inmueble
    """
    vigilancia = models.BooleanField(null = True, blank = True)
    parqueadero = models.BooleanField(null = True, blank = True)
    salon_social = models.BooleanField(null = True, blank = True)
    numero_pisos = models.IntegerField()

class inmueble(models.Model):
    """
    Informacion completa del inmueble
    """
    tipo = models.CharField(max_length=50)
    subtipo = models.CharField(max_length=50)
    gen = models.ForeignKey(general, on_delete = 'CASCADE')
    inte = models.ForeignKey(interior, on_delete = 'CASCADE')
    ext = models.ForeignKey(exterior, on_delete = 'CASCADE')

    class Meta:
        ordering = ['tipo', 'subtipo',] #Ordena los registros por tipo y luego por subtipo
