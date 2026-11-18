# Documento de Visión y Especificación de Requisitos (SRS)

## 1. Planteamiento del Problema
Cuando una aplicación web recibe muchas solicitudes de forma simultánea (por ejemplo, cuando varios usuarios intentan acceder a un sistema), el servidor puede bloquearse o verse desbordado si no existe un mecanismo organizado. En entornos reales se emplean equilibradores de carga y colas de prioridad. Este proyecto cubre la falta de una herramienta educativa en Python que simule cómo llegan solicitudes de distintos tipos de usuarios (`Premium` frente a `Gratuitos`), cómo se organizan en colas según su prioridad, cómo el servidor las procesa teniendo en cuenta la latencia y cómo gestiona las solicitudes rechazadas por saturación.

## 2. Alcance del Proyecto
* **Lo que hace:** Simula el ciclo de vida de peticiones concurrentes mediante listas en Python (`append`, `pop(0)`), diferencia prioridades, procesa solicitudes simulando retrasos de tiempo y calcula métricas finales (tiempo medio de espera, tasa de atención y rechazos).
* **Lo que no hace:** No se conecta a bases de datos reales ni maneja solicitudes de red reales (es un script educativo que corre localmente en consola con gráficos básicos).

## 3. Objetivos
* **Objetivo Principal:** Implementar un simulador en Python basado en la teoría de colas para demostrar el equilibrio y la priorización del tráfico de solicitudes.
* **Objetivos Específicos:**
  * Gestionar listas de Python como colas de espera.
  * Implementar una lógica de prioridades para atender primero a los usuarios más importantes.
  * Calcular y mostrar métricas de rendimiento del servidor al finalizar la simulación.

## 4. Tabla de Requisitos del Sistema

| Código | Tipo | Nombre | Descripción |
| :--- | :--- | :--- | :--- |
| **RF-01** | Funcional | Generación de peticiones | Permitir ingresar o generar automáticamente peticiones clasificadas por prioridad (`Premium` y `Gratis`). |
| **RF-02** | Funcional | Organización en colas | Almacenar las solicitudes en colas separadas en memoria según su tipo de prioridad. |
| **RF-03** | Funcional | Control de balanceo y saturación | Evaluar si la cola supera su límite máximo; si está llena, rechazar la petición entrante para evitar el colapso. |
| **RF-04** | Funcional | Procesamiento secuencial | Extraer peticiones respetando prioridad y simular latencia mediante funciones de tiempo de Python. |
| **RF-05** | Funcional | Cálculo de métricas finales | Mostrar un reporte con tiempo medio de espera, tasa total de atención exitosa y número de rechazos. |
| **RNF-01** | No Funcional | Lenguaje y estructuras | Desarrollado íntegramente en Python usando listas (`append`, `pop(0)`), bucles y funciones. |
| **RNF-02** | No Funcional | Interfaz e interacción | Ejecución fluida en consola con representación gráfica opcional mediante `Matplotlib`. |
| **RNF-03** | No Funcional | Documentación del código | Incluir comentarios claros en cada bloque importante para facilitar su lectura académica. |
