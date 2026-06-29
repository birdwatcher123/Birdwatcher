import os #Import OS-Bibliothek (Funktionen des Betriebssystems)
import logging #Import Logging-Bibliothek
import shutil #Import Shutil-Bibliothek (Datei- und Ordneroptionen)

class folder:
    
    
  #  def __init__():
        #logging.basicConfig(filename="folder_log.txt", format="%(asctime)s %(message)s")
        #year = datetime.now().strftime("%Y")
        #month = datetime.now().strftime("%m-%Y")
        
            
    def createFolder(pPath): # Erstellung eines Ordners, mit Pfad als Parameter

        if not os.path.exists(pPath): #"Wenn Ordner noch nicht existiert"
            try:
                os.mkdir(pPath) #Erstelle Ordnern
            except OSError as error:
                logging.error(error) #Logging potentieller Fehlermeldung

    def delFolder(pTransfer): # Löschen eines Ordners, mit Pfad als Parameter
        try:
            shutil.rmtree(pTransfer) # Lösche Ordner
        except Exception as e:
            logging.error(e) #Logging potentieller Fehlermeldung
                    
            
    def transfer (pFile, pTransfer): # Kopieren einer Datei an einen anderen Ort, Dateipfad und Kopierpfad als Parameter
        
        try:
            shutil.copy(pFile, pTransfer) # Kopiere Datei
            #shutil.make_archive(pTransfer,'zip', pTransfer)
        except Exception as e:
            logging.error(e) #Logging potentieller Fehlermeldung
            
    def compress(pTransfer): # Komprimierung einer Datei, eines Ordners als Zip. Pfad als Parameter
        
        try:
            shutil.make_archive(pTransfer,'zip', pTransfer) # Komprimierung, Speicherung des .zip an dem gleichen Ort
        except Exception as e:
            logging.error(e) #Logging potentieller Fehlermeldung
