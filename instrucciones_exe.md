# Cómo convertir el repositorio en ejecutable

## 1. Navegar al directorio en dónde queremos crear el .exe

command prompt: ir a la carpeta de documentos en donde tenemos nuestro proyecto

Documentos -> Github -> Guerra de Meteoros -> [main.py]
** Importante! revisar que el main.py sea la versión del código que queremos

<!-- cmd + Enter -->

## 2. Instalar librerías
<!-- pip install pyinstaller -->
si no funciona correctamente, probar
<!-- pip install PyInstaller -->

## 3. Revisar en dónde está nuestro main.py
Como tenemos varias carpetas con distintas versiones del juego, debemos revisar en qué carpeta está la versión final
* es útil "sacar" esa versión de su carpeta y dejarla en "Guerra de Meteoros"

## 4. Crear el ejecutable con PyInstaller
<!-- pyinstaller [opciones] myscript.py -->

esto creará un folder 'dist' dentro del cuál guardará el 'myscript.exe'

### Cambiar el path en donde queremos que se guarde
pyinstaller "C:\Documents and Settings\project\myscript.spec"

### Opciones de pyinstaller (flags)
<!-- -F, --onefile --> Guarda todo el proyecto en un solo archivo
<!-- -D, --onedir --> Crea una carpeta con todo el contenido del ejecutable (opción por defecto)
<!-- -n, --name NAME --> Asigna un nombre distinto al archivo
<!-- --windowed --> Crea una ventana para visualizar el archivo (permite identificar errores)

## 5. Buscar el .exe en el directorio 'dist'
* ¿Se puede ejecutar el juego?
* CREAR NUEVAMENTE
'' pyinstaller myscript.py --onefile --windowed ''

* se ejecutará más rápido porque ya tenemos muchos de los archivos necesarios

*¿Qué error nos arroja la ventana?*

## 6. Mover el ejecutable al directorio principal

Documentos -> Github -> Guerra de Meteoros -> dist -> myscript.exe

debe cambiar a:

Documentos -> Github -> Guerra de Meteoros -> myscript.exe

## 7. Revisar si todo funciona bien
* ¿se guardaron todos los cambios que le habían hecho a su script?
* ¿las imágenes son correctas?
* ¿el sistema de puntos/niveles funciona bien?
* ¿se escucha la música?

en resumen:
**¿El juego está listo para ser mostrado al público?**

## 8. Guardar todo en un .zip
* Es más sencillo compartir solamente un archivo, para ello podemos comprimir el ejecutable + la carpeta de elementos gráficos. Usar 'Comprimir en archivo ZIP''

## 9. Subir a GitHub y/o Google Drive

## 10. Compartir con tus amigos :D
## ¡Probemos los juegos de los demás!