from datetime import datetime # Import Datetime-Bibliothek, für den Umgang mit Daten und Zeiten
from folder import * # Import folder.py
from camera import * # Import camera.py
from transfer import * # Import transfer.py
import logging # Import Logging-Bibliothek zum Erstellen einer Logdatei

class Process():

    def __init__(self): # Ausführung beim Programmaufruf
                                                                                                        # DD-MM-YYYY_HH-MM-SS
        time = datetime.now().strftime("%d-%m-%Y_%H-%M-%S") # Erstellung der aktuell Uhrzeit im Format "03-10-2022_20-13-23"
        year = datetime.now().strftime("%Y") # Erstellung des Jahres als Text
        month = datetime.now().strftime("%m-%Y") # Erstellung des Monates und Jahres als Text
        path1 = '/home/birdwatcher/Desktop/Birdwatcher_Bilder' # Ordnerpfad 1 [zu ergänzen]
        path2 = '/home/birdwatcher/Desktop/Birdwatcher_Bilder/%s' % year # Ordnerpfad 2 [zu ergänzen]
        path3 = '/home/birdwatcher/Desktop/Birdwatcher_Bilder/%s/%s' % (year, month) # Ordnerpfad 3 [zu ergänzen]
        pFile = path3 + '/image_' + time + '.jpg' # Dateipfad für die Aufnahme
        filename = time + '.zip' # Dateiname für den Mail-Versand

        pSubject = 'Vogelbeobachtung ' + time # Betreff der E-Mail
        pFrom = 'birdwatcher@smart-mail.de' # Absenderadresse der Mail [zu ergänzen]
        pTo = 'birdwatcher.ium@hsbi.de' # Empfaengeradresse [zu ergänzen]
        pContent = 'Foto aus dem Nistkasten' # E-Mailtext [zu ergänzen]
        host = 'smtp.smart-mail.de' # SMTP-Url des Mailproviders [zu ergänzen]
        username = 'birdwatcher@smart-mail.de' # Benutzername des Mail-Kontos
        
        send_mails= False 

        # Passwort aus Textdatei lesen
        try:
            with open('/home/birdwatcher/Birdwatcher/Birdwatcher/mail_password.txt', 'r') as f:
                password = f.read().strip()
        except Exception as e:
            logging.error("Passwort-Datei konnte nicht gelesen werden: " + str(e))
            password = ""
        
        pTransfer = '/home/birdwatcher/Desktop/Birdwatcher_Bilder/transfer' # Ordnerpfad für den Transferordner
        logging.basicConfig(filename="process_log.txt", format="%(asctime)s %(message)s") # Erstellung und Konfiguration der Log-Datei

        #folder.delFolder('/home/pi/Desktop/Birdwatcher')
        folder.createFolder(path1) # Erstellung des Ordners an Pfad 1
        folder.createFolder(path2) # Erstellung des Ordners an Pfad 2
        folder.createFolder(path3) # Erstellung des Ordners an Pfad 3
        folder.createFolder(pTransfer) # Erstellung des Transferordners

        camera.takePhoto(pFile) # Aufnahme und Speicherung unter dem Dateipfad

        
        if send_mails:
                folder.transfer(pFile, pTransfer) # Kopieren der Aufnahme in den Transferordner
                transfer.sendMail(pSubject, pFrom, pTo, pContent, pTransfer, filename, host, username, password) # Versand der Datei per E-Mail in einer .zip-Datei
        else:
                folder.transfer(pFile, pTransfer) # Kopieren der Aufnahme in den Transferordner
                
                print ("nix gesendet")
                
Process() # Klasse instanziieren und __init__ ausführen
