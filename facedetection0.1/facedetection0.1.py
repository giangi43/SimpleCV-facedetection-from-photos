import os
import glob
import time
from SimpleCV import *

#setto le variabili generali come i contatori e i colori e l'estensione immagine preferia "chase sensitive" o come si scrive

extension = "*.png"
fmatches = 0
ematches = 0
green = (0, 255, 0)
red = (255,0,0)



imgs = list() #creo una lista di immagini
#completo il path da cui estrarrò le foto
directory = os.path.join(os.path.join(os.getcwd(), "pictures"), extension)
#assegno una lista di path 
files = glob.glob(directory)
#assegno gli xml allenati a riconoscere volti e occhi
facexml =os.path.join(os.path.join( os.getcwd(), "data") , "haarcascade_frontalface_alt.xml")
eyexml = os.path.join(os.path.join( os.getcwd(), "data") , "haarcascade_eye.xml")

#esegu il ciclo per tutti i path presenti nella lista
for file in files:

        #prendo il tempo d' inizio dell ciclo
        tstart = time.time()

        #metto una singola inmmagine in una variabile per poterla elaborare e successivamente la ridimensiono 
        new_img = Image(file)
        new_img = new_img.resize(w=640,h=480)
          
        #rilevo i volti all interno dell immagine
        #facedetect = new_img.findHaarFeatures('C:/opencv/sources/data/haarcascades/haarcascade_frontalface_alt.xml')
        facedetect = new_img.findHaarFeatures(facexml)
        #eyedetect = new_img.findHaarFeatures("C:/opencv/sources/data/haarcascades/haarcascade_eye.xml")
        eyedetect = new_img.findHaarFeatures(eyexml)
 
                 #se trovo volti o occhi conto e evidenzio
        if facedetect:
                         #per tutti i volti rilevati
          for f in facedetect:
              #incremento il contatore
              fmatches += 1
                # evidenzio con un rettangolo 
              facedetect.sortColorDistance(green).draw(green)  
                                  
        if eyedetect:
            for e in eyedetect:                
                ematches += 1
                eyedetect.sortColorDistance(red).draw(red)
        
        #mostro l'immagine
        new_img.show()
                       
        #stampo il numero di volti e di occhi rilevati
        print "faces: " + str(fmatches) + "; eye:" + str(ematches)
        #azzero i contatori di volti e ochhi
        fmatches = 0
        ematches = 0
        #prendo il tempo di fine ciclo
        tfinish = time.time()
        #stampo la sottrazione tra il tempo finale ed il tempo iniziale per sapere quanto tempo prende un singolo cilo 
        print str(tfinish-tstart)              

        #aspetto un secondo per vedere la foto
        time.sleep(1)
sys.exit()