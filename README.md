# Inmobilio_venv

**Prueba tecnica de ingreso para la empresa Inmobilio**

Consiste en una pagina web sencilla para probar mis conocimientos de BACKEND con Django y Django Restframework. Siendo implementada en un entorno virtual de tipo **Pipenv** y ademas usando los contenedores docker.

Se implemento un CRUD (Create, Read, Update, Delete)
para una base de datos que contiene 4 tablas (inmueble, general, interior, exterior), la cual cumple a la siguiente estructura JSON:

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

La pagina se desarrollo con las abstracciones de Django Restframework, de esta manera se utilizo muy poco codigo
y se dieron las funciones de:
* Listar inmuebles
* Detallar inmueble individual
* Modificar inmueble
* Crear Inmueble
* Eliminar Inmueble

Para la **documentacion** (ademas de los comentarios dentro del codigo) se realizo una sencilla implementacion de *Django-Rest-Swagger* la cual se puede observar en el endpoint:
- api/doc  

Todo la implementacion se realizo dentro de un entorno virtual tipo **Pipenv**, y este entorno a su vez
fue implementado dentro de un contenedor *Docker*.  
Para la base de datos tipo **PostgreSQL**, se implemento otro contenedor *Docker*, y se enlazaron los dos para poder ingresar a la base de datos.

### Problemas encontrados

Se recomendaba hacer un fork del [repositorio original](https://gitlab.com/inmobilio-interview/backend-python/tree/master),  
**PERO** presentaba algunos errores como por ejemplo con la libreria *GDAL* la cual no permitio ser instalada de ninguna manera  
dentro del entorno virtual **Pipenv**.   
Tambien se considero que el archivo Pipfile tenia algunas librerias que no eran completamente necesarias para el desarrollo de la prueba.  

Por lo tanto el proyecto se desarrollo de cero, y se obtuvo un nuevo archivo *Pipfile* y por supuesto un nuevo archivo *Pipfile.lock*.  
Se construyeton dos archivos:
* Dockerfile
* docker-compose.yml
los cuales permiten la creacion de los contenedores para el despliegue de la aplicacion.

# Instrucciones para lanzar la aplicacion.

Estas instrucciones se dan suponiendo que se tiene instalado Docker y docker-compose en el equipo.

1. sudo docker-compose up  
2. En el navegador buscar localhost:9000

Y ya esta, asi de facil se despliega la aplicación.
