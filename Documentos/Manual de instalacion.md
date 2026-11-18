# Manual de Instalación y Despliegue

## 1. Requisitos del Sistema
* **Sistema Operativo:** Windows 10/11, macOS o Linux.
* **Lenguaje:** Python 3.10 o superior instalado y agregado al `PATH` del sistema.
* **Editor recomendado:** Visual Studio Code.

## 2. Pasos de Instalación
1. Descarga o clona el repositorio del proyecto en una carpeta local.
2. Abre una terminal o consola de comandos dentro de la carpeta del proyecto.
3. Instala las librerías requeridas ejecutando:
   ```bash
   pip install -r requirements.txt
   ```
4. Inicia la aplicación con el comando:
   ```bash
   python main.py
   ```

## 3. Configuración de Parámetros (Equivalente a variables de entorno)
Dado que el proyecto opera de forma local en memoria sin conexiones a red ni motores de bases de datos externos, no requiere un archivo `.env` con credenciales o puertos. 

Para ajustar el comportamiento de la simulación, modifica las constantes ubicadas en la cabecera del archivo `main.py`:
* `LIMITE_SATURACION = 6`: Define la capacidad máxima total permitida entre ambas colas antes de rechazar tráfico.
* `TOTAL_PETICIONES = 15`: Define la cantidad de solicitudes concurrentes generadas por ciclo de prueba.
