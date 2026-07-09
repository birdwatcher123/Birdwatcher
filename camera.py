from picamera2 import Picamera2  
import logging
from time import sleep

class camera():

    def takePhoto(pFile):  # pFile = Speicherort des Fotos

        try:
            camera = Picamera2()
            

            camera.video_configuration.transform.vflip = True
            camera.video_configuration.transform.hflip = True
            
            config = camera.create_still_configuration()  
            camera.configure(config)
            
            camera.start()        # Kamera starten
            sleep(2)              
            camera.capture_file(pFile)  # Foto aufnehmen und speichern
            camera.stop()         # Kamera stoppen
            camera.close()        # Kamera freigeben
            
        except Exception as a:
            logging.error(a)
