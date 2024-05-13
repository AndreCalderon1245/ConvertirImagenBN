import Ice
import sys
from PIL import Image

Ice.loadSlice('ImageConverter.ice')
import ImageConverter

class ConverterI(ImageConverter.Converter):
    def convertToBlackAndWhite(self, inputFile, outputFile, current=None):
        try:
            # Abrir la imagen de entrada usando Pillow
            img = Image.open(inputFile)
            # Convertir la imagen a escala de grises
            img = img.convert('L')
            # Guardar la imagen en blanco y negro en el archivo de salida
            img.save(outputFile)
            print(f"Imagen convertida guardada en: {outputFile}")
        except Exception as e:
            print(f"Error al convertir la imagen: {str(e)}")

with Ice.initialize(sys.argv) as communicator:
    adapter = communicator.createObjectAdapterWithEndpoints("ImageConverterAdapter", "default -p 10000")
    adapter.add(ConverterI(), Ice.stringToIdentity("ImageConverter"))
    adapter.activate()
    communicator.waitForShutdown()
