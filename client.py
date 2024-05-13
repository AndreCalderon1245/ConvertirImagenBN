import Ice
import sys
import os

Ice.loadSlice('ImageConverter.ice')
import ImageConverter

def get_downloads_folder():
    # Función para obtener la ruta de la carpeta de descargas del usuario
    downloads_folder = os.path.join(os.path.expanduser('~'), 'Downloads')
    return downloads_folder

def get_user_input():
    # Solicitar la ruta de la imagen de entrada y el nombre del archivo de salida al usuario
    input_path = input("Ingrese la ruta de la imagen de entrada (puede ser JPG o PNG): ")
    output_name = input("Ingrese el nombre del archivo de salida para la imagen convertida: ")
    return input_path, output_name

with Ice.initialize(sys.argv) as communicator:
    base = communicator.stringToProxy("ImageConverter:default -p 10000")
    converter = ImageConverter.ConverterPrx.checkedCast(base)
    if not converter:
        raise RuntimeError("Error al obtener el proxy del servidor Ice")

    # Obtener la ruta de la imagen de entrada y el nombre del archivo de salida desde la entrada del usuario
    input_path, output_name = get_user_input()

    # Obtener la ruta completa del archivo de salida en la carpeta de descargas
    downloads_folder = get_downloads_folder()
    output_file = os.path.join(downloads_folder, output_name)

    # Llamar al método para convertir la imagen a blanco y negro
    converter.convertToBlackAndWhite(input_path, output_file)
    print(f"Imagen convertida guardada en: {output_file}")
