# Importa dxcam per catturare lo schermo
import dxcam
# Importa OpenCV per salvare il video
import cv2
# Importa NumPy per manipolazione array (frame)
import numpy as np
# Importa pyautogui come fallback per ottenere dimensione schermo
import pyautogui

# Crea un'istanza della camera (cattura schermo)
camera = dxcam.create()

# Ottieni le dimensioni dello schermo in modo sicuro
try:
    # dxcam fornisce le dimensioni del monitor target
    screen_width, screen_height = camera.target.width, camera.target.height
except AttributeError:
    # Se dxcam non riesce, usa pyautogui come fallback
    screen_width, screen_height = pyautogui.size()

# Definisce il codec video e il writer per salvare in MP4
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec MP4
out = cv2.VideoWriter('screen_record.mp4', fourcc, 30.0, (screen_width, screen_height))

# Avvia la cattura continua con dxcam
camera.start()

try:
    # Ciclo infinito per scrivere frame nel video
    while True:
        frame = camera.get_latest_frame()  # Ottieni l'ultimo frame catturato
        if frame is not None:
            # dxcam cattura in RGB, OpenCV usa BGR: conversione necessaria
            frame_bgr = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
            # Scrive il frame nel file video
            out.write(frame_bgr)

# Permette di interrompere con Ctrl+C
except KeyboardInterrupt:
    print("Stopping recording...")

# Ferma la cattura e rilascia il file video
camera.stop()
out.release()
