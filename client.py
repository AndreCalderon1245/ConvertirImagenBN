import Ice
import sys
import base64
import os

# Importar la interfaz generada por Ice
import ImageProcessing

# Configurar Ice
with Ice.initialize(sys.argv) as communicator:
    # Crear un proxy con la dirección IP específica
    proxy_str = "ImageProcessor:tcp -h 192.168.0.23 -p 10000"
    base = communicator.stringToProxy(proxy_str)
    image_processor = ImageProcessing.ImageProcessorPrx.checkedCast(base)
    if not image_processor:
        raise RuntimeError("Invalid proxy")
    
    # Solicitar al usuario la ruta de la imagen
    image_path = input("Ingrese la ruta de la imagen: ")
    
    # Verificar si la ruta de la imagen es válida
    if not os.path.exists(image_path):
        print("La ruta de la imagen no es válida.")
        sys.exit(1)
    
    # Leer la imagen desde la ruta proporcionada
    with open(image_path, "rb") as f:
        image_data = f.read()
    
    # Codificar la imagen en base64
    image_data_base64 = base64.b64encode(image_data).decode()
    
    # Llamar al método en el servidor para procesar la imagen
    processed_image_base64 = image_processor.processImage(image_data_base64)
    
    # Decodificar la imagen procesada de base64
    processed_image_data = base64.b64decode(processed_image_base64)
    
    # Obtener la ruta de la carpeta de descargas del usuario
    downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")
    
    # Generar la ruta de la imagen procesada en la carpeta de descargas
    processed_image_path = os.path.join(downloads_folder, "processed_image.jpg")
    
    # Guardar la imagen procesada en la carpeta de descargas
    with open(processed_image_path, "wb") as f_processed:
        f_processed.write(processed_image_data)
    
    print(f"La imagen procesada se ha guardado en: {processed_image_path}")
