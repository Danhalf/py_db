import os
import subprocess
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class FileChangeHandler(FileSystemEventHandler):
    def __init__(self, script):
        self.script = script
        self.process = None
        self.restart_script()

    def on_modified(self, event):
        if event.src_path.endswith(".py"):
            print("Changed detected in {}. Restarting script...".format(event.src_path))
            self.restart_script()

    def restart_script(self):
        if self.process:
            self.process.terminate()
            self.process.wait()

        self.process = subprocess.Popen(['python', self.script])

if __name__ == "__main__":
    script_name = "app.py" 
    path = os.path.dirname(os.path.abspath(__file__))

    event_handler = FileChangeHandler(script_name)
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        if event_handler.process:
            event_handler.process.terminate()

    observer.join()
