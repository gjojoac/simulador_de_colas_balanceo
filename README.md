# Simulador de Colas de Servidor y Balanceo de Carga

Herramienta educativa desarrollada en **Python** que modela el comportamiento de un servidor web frente a múltiples solicitudes concurrentes, implementando colas de prioridad (`Premium` y `Gratis`), control de saturación y métricas de rendimiento en tiempo real.

## Estructura del Proyecto
* `main.py`: Código fuente principal del simulador y generación de gráficas.
* `requirements.txt`: Dependencias necesarias para ejecutar el entorno.
* `Datos de prueba.csv`: Conjunto de datos iniciales de prueba.
* [Documento de Visión (SRS)](Documentos/Documento%20vision%20SRS.md): Planteamiento del problema, alcance, objetivos y requisitos.
* [Manual de Usuario](Documentos/Manual%20de%20usuario.md): Guía paso a paso para operar el simulador.
* [Manual de Instalación](Documentos/Manual%20de%20instalacion.md): Instrucciones técnicas de despliegue y configuración.
* [Manual Técnico](Documentos/Manual%20tecnico.md): Arquitectura del software y diagrama de flujo.
* [Acta de Entrega](Documentos/Acta%20de%20entrega.md): Formato de aceptación y conformidad del proyecto.

## Ejecución Rápida
1. Instalar dependencias: `pip install -r requirements.txt`
2. Ejecutar el simulador: `python main.py`
'