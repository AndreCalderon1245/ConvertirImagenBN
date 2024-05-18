import Ice
import sys
import base64
from PIL import Image
from io import BytesIO

# Importar la interfaz generada por Ice
import ImageProcessing

class ImageProcessorI(ImageProcessing.ImageProcessor):
    def processImage(self, imageDataBase64, current=None):
        # Decodificar la imagen de base64
        image_data = base64.b64decode(imageDataBase64)
        
        # Convertir la imagen a blanco y negro
        img = Image.open(BytesIO(image_data))
        img_bw = img.convert("L")
        
        # Guardar la imagen en blanco y negro como base64
        buffered = BytesIO()
        img_bw.save(buffered, format="JPEG")
        img_bw_base64 = base64.b64encode(buffered.getvalue()).decode()
        
        # Devolver la imagen en blanco y negro como base64
        return img_bw_base64

# Configurar Ice
with Ice.initialize(sys.argv) as communicator:
    adapter = communicator.createObjectAdapterWithEndpoints("ImageProcessorAdapter", "default -h 192.168.0.23 -p 10000")
    object = ImageProcessorI()
    adapter.add(object, communicator.stringToIdentity("ImageProcessor"))
    adapter.activate()
    communicator.waitForShutdown()
