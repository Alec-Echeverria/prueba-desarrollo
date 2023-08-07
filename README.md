<style>
  h2 {
    color: #5DADE2;
  }

  h1{
    color:#00C000 
  }
  
</style>


# APLICACIÓN GESTION DE PREDIOS & PROPIETARIOS

Este código define tres modelos en Django: `Propietario`, `Predio`, y `PropietarioPredio`. Los modelos representan propietarios, predios y la relación entre ellos.

- El modelo `Propietario` tiene campos como nombre, tipo de identificación, número de identificación y tipo de propietario. Además, tiene una relación Many-to-Many con el modelo `Predio`.

- El modelo `Predio` tiene campos como dirección, tipo de predio, número de catastro y número de matrícula. También tiene una relación Many-to-Many con el modelo `Propietario`.

- El modelo `PropietarioPredio` representa la relación entre propietarios y predios. Tiene dos campos de clave foránea que apuntan a los modelos `Propietario` y `Predio`.

Además, el código proporciona serializadores para convertir los objetos de los modelos en formato JSON y vistas basadas en clases para realizar operaciones CRUD en los modelos a través de la API.

<h1 style="color:gray">Indice</h1> 

1. [¿Como instalar la api?](#sesión-1)
2. [Gestion de predios & usuarios de la api](#sesión-2)
3. [Notas adicionales.](#sesión-3)
4. [Script de extracion de códigos de anotaciones.](#sesión-4)

## ¿Cómo instalar la API y los recursos necesarios?

A continuación, te proporciono los pasos necesarios para instalar la API creada en Django:

1. **Clonar el repositorio:** Para empezar, abre la terminal y utiliza el siguiente comando para clonar el repositorio en tu máquina local: `git clone URL_del_repositorio`

2. **Instalar dependencias:** Antes de continuar, asegúrate de tener un entorno virtual configurado con tu gestor de ambientes preferido. Activa el entorno virtual y luego instala las dependencias requeridas para el proyecto. Para ello, ejecuta el siguiente comando en la terminal: `pip install -r requirements.txt`

3. **Configurar la base de datos:** Por defecto, el proyecto está configurado para utilizar la base de datos SQLite 3 de desarrollo de Django. Sin embargo, también tienes la opción de utilizar una base de datos PostgreSQL. Si deseas usar PostgreSQL, comenta las líneas relacionadas con la base de datos SQLite y descomenta las de PostgreSQL en el fichero **settings.py**. Luego, proporciona los datos necesarios, como el nombre de la base de datos, el usuario, etc., para que la aplicación pueda conectarse.

4. **Generar las respectivas migraciones:** Asegúrate de que la base de datos esté correctamente configurada y luego ejecuta el siguiente comando en la terminal para generar las migraciones necesarias: `python manage.py migrate`

5. **Crear superusuario (opcional):** Si deseas gestionar los modelos generados de manera más rápida y a través de una interfaz, puedes crear un superusuario. Para hacerlo, utiliza el siguiente comando: `python manage.py createsuperuser`

6. **Ejecutar el servidor:** Estamos casi listos. Ahora, para poner en marcha la API, ejecuta el servidor mediante el siguiente comando: `python manage.py runserver`. Una vez que el servidor esté en funcionamiento, podrás realizar peticiones HTTP a las siguientes URLs:

- `api/predios/`
- `api/predios/<int:pk>/`
- `api/propietarios/`
- `api/propietarios/<int:pk>/`

Recuerda anteponer a las urls el fragmento `api/`, un ejemplo de como deberia quedar tu url es:<br/>
`[http://tu-dominio.com/api/propietarios/`

Sigue estos pasos y podrás instalar y utilizar la API de Django sin problemas
<h2 style="color:gray">¡Buena suerte!</h2>

## Gestion de predios & usuarios de la api
**GESTION DE PREDIOS**

1. **Crear Predios**<br/>
Para crear un predio, sigue estos pasos:

- Accede a la vista generada en la siguiente URL: [http://tu-dominio.com/predios/](http://tu-dominio.com/predios/)

- En esta vista, podrás visualizar todos los predios que ya han sido creados. Cada predio se muestra con su respectivo nombre o dirección, un tipo (Urbano o Rural), un número catastral único de 30 dígitos y un número de matrícula inmobiliaria, que también es único. Además, se encuentran los propietarios asociados al predio.

- Para crear un nuevo predio, utiliza la operación "Create" a través del método POST en la API.

**Nota:** El número de catastro se tomará como el identificador (ID) del predio.

2. **Acceder a un Predio Específico**
Si deseas realizar peticiones PUT o DELETE para un predio específico, puedes acceder a la vista utilizando la siguiente URL: [http://tu-dominio.com/predios/<int:pk>/](http://tu-dominio.com/predios/<int:pk>/), donde `pk` es el número de identificación del predio.

**GESTIÓN DE PROPIETARIOS**

1. **Crear Propietarios**<br/>
Para crear un propietario, sigue estos pasos:

- Accede a la vista generada en la siguiente URL: [http://tu-dominio.com/propietarios/](http://tu-dominio.com/propietarios/)
- Introduce los datos del nuevo propietario.
- Tienes la opción de asociar uno o más predios creados previamente al propietario.

**Nota:** El número de cédula se tomará como el identificador (ID) del propietario.

2. Asociar Predios a un Propietario
Una vez creado el propietario, puedes asociarle predios existentes siguiendo estos pasos:

- Valida la lista de predios existentes para seleccionar aquellos que deseas asociar al propietario.

3. **Acceder a un Propietario Específico**
Si deseas eliminar o editar un propietario creado, puedes acceder a la vista utilizando la siguiente URL: [http://tu-dominio.com/propietarios/<int:pk>/](http://tu-dominio.com/propietarios/<int:pk>/), donde `pk` es el número de identificación del propietario.

De esta manera, puedes gestionar los predios y propietarios de manera eficiente a través de la API.

## Notas adicionales.
Se ha creado una guia con imagenes en drive para tener mayor claridad y/o despejar dudas, esta viene incluida en el repositorio con el nombre de `guia_de_uso_basic.pdf`

## Script de extracción de códigos de anotaciones

En este repositorio también encontrarás una carpeta llamada `script_extracion` donde se encuentra `extractor_anotaciones.py` y una subcarpeta llamada `archivos_analizar` donde hay archivos JSON de prueba. El archivo `extractor_anotaciones.py` es el script encargado de generar diccionarios de la siguiente forma:

```json
{
    "fmi": "442-14369",
    "anotaciones": [
        {
            "numero": 1,
            "codigo_especificacion": "101"
        },
        {
            "numero": 2,
            "codigo_especificacion": "0126"
        },
        {
            "numero": 3,
            "codigo_especificacion": "0913"
        }
    ]
}
```
El diccionario contiene el atributo "fmi", que es una combinación del valor de "circulo" y "numeroMatricula", y una lista de anotaciones con sus respectivos números y códigos de especificación.

### Uso del script

Para utilizar el script, sigue estos pasos:

1. Asegúrate de tener Python instalado en tu sistema.

2. Copia el contenido del script `extractor_anotaciones.py` en un archivo de texto con extensión ".py", ya sea utilizando un editor de texto o un entorno de desarrollo integrado (IDE).

3. En el bloque `if __name__ == "__main__":`, establece el valor de la variable `nombre_json` con la ruta y nombre del archivo JSON que deseas procesar. Por ejemplo, puedes cambiar `nombre_json = 'script_extracion/archivos_analizar/132-22359.json'` por la ruta y nombre del archivo JSON que deseas analizar.

4. Ejecuta el script Python utilizando el comando `python nombre_del_archivo.py` desde la terminal o línea de comandos.

5. El script cargará el archivo JSON especificado, procesará los datos y generará el diccionario de salida. Si se produce algún error, como un archivo no encontrado o un JSON no válido, el script mostrará un mensaje de error correspondiente.

6. Dependiendo de tus necesidades, puedes utilizar la variable `data_procesada` para acceder a los datos procesados y realizar cualquier operación adicional que desees.

Es importante asegurarse de que el archivo JSON contenga los campos requeridos ("circulo", "numeroMatricula" y "textoAnotaciones") y que la estructura del archivo esté en el formato esperado para que el script funcione correctamente. Además, el script utiliza un bloque `try-except` para manejar posibles errores y garantizar un comportamiento robusto en caso de que algo salga mal durante el proceso de extracción y generación del diccionario.
