# Importa dxcam per catturare lo schermo
import dxcam
# Importa PIL per manipolare e salvare immagini
from PIL import Image
# Importa os per lavorare con percorsi di file
import os
# Importa time per gestire i ritardi
import time
# Importa datetime per creare timestamp unici
from datetime import datetime

# Crea un oggetto camera, collegato al monitor principale
camera = dxcam.create()  # Ritorna un'istanza DXCamera

# Ottieni la cartella in cui si trova questo script per salvare gli screenshot
script_folder = os.path.dirname(os.path.abspath(__file__))

try:
    # Ciclo infinito per catturare screenshot continuamente
    while True:
        # Cattura un frame dallo schermo
        frame = camera.grab()
        
        # Converti il frame (array NumPy) in un'immagine PIL
        img = Image.fromarray(frame)
        
        # Genera un nome file unico basato su data e ora corrente
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_path = os.path.join(script_folder, f"screenshot_{timestamp}.png")
        
        # Salva l'immagine nel percorso specificato
        img.save(file_path)
        
        # Attende 60 secondi prima di catturare il prossimo screenshot
        time.sleep(60)

# Permette di fermare il ciclo premendo Ctrl+C
except KeyboardInterrupt:
    print("Screenshot script stopped.")
