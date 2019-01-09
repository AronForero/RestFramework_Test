# Inmobilio_venv

**Prueba tecnica para el ingreso a la empresa de inmobiliaria Inmobilio**

Consiste en una pagina web sencilla para probar mis conocimientos de BACKEND con Django y Django Restframework.  

Se implemento un CRUD (Create, Read, Update, Delete)
para una base de datos que contenga 4 tablas (inmueble, general, interior, exterior) la cual cumple a la siguiente estructura JSON:

~~~
{
  "inmueble": {
    "tipo": "string",
    "subtipo": "string",
    "general": {
      "direccion": "string",
      "ciudad": "string",
      "departamento": "string",
      "pais": "string",
      "telefono": "string"
    },
    "interior": {
      "cuartos": "float",
      "baños": "integer",
      "closets": "integer",
      "calentador": "boolean"
    },
    "exterior": {
      "vigilancia": "string",
      "parqueadero": "string",
      "salon_social": "boolean",
      "numero_pisos": "integer"
    }
  }
}
~~~

La base de datos se implemento con PostgreSQL, en el puerto 5433 (por defecto 5432, si es necesario cambiar el puerto en backend/settings.py), con el usuario 'admin', contraseña '123456' y una base de datos llamada 'inmobilio'.  
La pagina se desarrollo con las implementaciones de Django Restframework, de esta manera se utilizo muy poco codigo
y se dieron las funciones de:
* Listar inmuebles
* Detallar inmueble individual
* Modificar inmueble
* Crear Inmueble
* Eliminar Inmueble

Todo la implementacion se realizo dentro de un entorno virtual tipo **Pipenv**.

### Problemas encontrados

Se recomendaba hacer un fork del [repositorio original](https://gitlab.com/inmobilio-interview/backend-python/tree/master),  
**PERO** presentaba algunos errores como por ejemplo con la libreria *GDAL* la cual no permitio ser instalada de ninguna manera  
dentro del entorno virtual **Pipenv**.   
Tambien se considero que el archivo Pipfile tenia algunas librerias que no eran completamente necesarias para el desarrollo  
de la prueba.

Por lo tanto el proyecto se desarrollo de cero, y se obtuvo un nuevo archivo *Pipfile* y por supuesto un nuevo archivo *Pipfile.lock*.

> Realmente nunca habia usado ni cacharreado nada con docker y tuve ciertos problemas por mi inexperiencia y mi desconocimiento de la herramienta por esta razon no implemente el proyecto dentro de un contenedor sino que lo deje simplemente en el entorno virtual **Pipenv**,  

No se entrego un archivo Dockerfile pero de igual manera se genero un archivo requirements.txt

### Finalmente
Solo me queda agradecer por la oportunidad, y espero una respuesta de su parte.
