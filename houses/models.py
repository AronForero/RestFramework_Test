from django.db import models

# Create your models here.
class general(models.Model):
    direccion = models.CharField(max_length=50)
    ciudad =  models.CharField(max_length = 30)
    departamento = models.CharField(max_length = 30)
    pais = models.CharField(max_length = 30)
    telefono = models.CharField(max_length = 10)

class interior(models.Model):
    cuartos = models.IntegerField()
    baños = models.IntegerField()
    closets = models.IntegerField()
    calentador = models.BooleanField(null = True, blank = True)

class exterior(models.Model):
    vigilancia = models.BooleanField(null = True, blank = True)
    parqueadero = models.BooleanField(null = True, blank = True)
    salon_social = models.BooleanField(null = True, blank = True)
    numero_pisos = models.IntegerField()

class inmueble(models.Model):
    tipo = models.CharField(max_length=50)
    subtipo = models.CharField(max_length=50)
    gen = models.ForeignKey(general, on_delete = 'CASCADE')
    inte = models.ForeignKey(interior, on_delete = 'CASCADE')
    ext = models.ForeignKey(exterior, on_delete = 'CASCADE')

    class Meta:
        ordering = ['tipo', 'subtipo',]
