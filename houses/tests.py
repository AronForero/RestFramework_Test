from django.test import TestCase
from .models import inmueble, general, interior, exterior
# Create your tests here.

class interior_test(TestCase):
    """
    Los tests no son realmente necesarios en esta aplicacion sencilla
    """
    def setUp(self):
        interior.objects.create(cuartos='3', baños='1', closets='2', calentador=False)
        interior.objects.create(cuartos='4', baños='2', closets='3', calentador=True)
