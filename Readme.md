# prueba_namtrik

Este repositorio contiene lo archvos fuente de la pureba tecnica de la empresa namtrik para desarrolladores backend django 

## Contenido

* `design`: Esta carpeta contiene los diagramas de clase, paquetes y despliegue del proyecto
* `sistema_seleccion_y_reclutamiento`: Esta carpeta contiene el codigo fuente del proyecto

##Diagramas

Los diagramas se realizaron en la herramienta staruml


## Proyecto django `sistema_seleccion_y_reclutamiento`: 

Para ejecutar el proyecto django en local ejecuta los siguientes comandos en una terminal dentro del directorio del proyecto.

```shell
pipenv install
pipenv shell
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

En la carpeta usuarios/fixtures, se encuentran 2 archvios .json, los cuales sirven para cargar usuarios al sistema, con los siguientes comandos:

python manage.py loaddata usuarios/fixtures/usuarios_empresa.json

python manage.py loaddata usuarios/fixtures/usuarios_aspirante.json

todos los usuarios tienen clave por defecto 'adminlocal123', y van con id del 2 al 9. El id 1 es para el superusuario que cree