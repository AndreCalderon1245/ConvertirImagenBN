# Aplicación de Conversión de Imágenes a Blanco y Negro con Ice

Este repositorio utiliza Ice (Internet Communications Engine) para permitir la conversión de imágenes a blanco y negro de forma distribuida entre un cliente y un servidor.

## Requisitos Previos

Antes de comenzar, asegúrate de tener instalados los siguientes requisitos:

- Python 3.x (se recomienda la versión más reciente)
- ZeroC Ice (instalado y configurado correctamente en tu sistema)

## Instalación de ZeroC Ice

Sigue estos pasos para instalar ZeroC Ice en tu sistema:

### 1. Descarga de ZeroC Ice

Visita el sitio web oficial de ZeroC Ice y descarga la versión adecuada para tu sistema operativo:
[ZeroC Ice Downloads](https://zeroc.com/products/ice)

### 2. Instalación en Windows

- Ejecuta el instalador descargado.
- Sigue las instrucciones del asistente de instalación.
- Asegúrate de seleccionar las opciones adecuadas para incluir las bibliotecas y herramientas necesarias para Python.

### 3. Instalación en macOS/Linux

- Descomprime el paquete descargado.
- Abre una terminal y navega al directorio descomprimido.
- Ejecuta el script de instalación proporcionado según las instrucciones específicas de Ice para macOS/Linux.

### Verificación de la Instalación

Después de instalar Ice, verifica si la instalación fue exitosa abriendo una terminal o línea de comandos y ejecutando los siguientes comandos:

```bash
slice2py --version
slice2py --slicedir
