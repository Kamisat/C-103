import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

origin = "C:/Users/Admin/Downloads"

class fileEventHandler(FileSystemEventHandler):

    def on_created(self, event):
        print(f"O arquivo {event.src_path} foi criado")
    def on_deleted(self, event):
        print(f"O arquivo {event.src_path} foi deletado")
    def on_modified(self, event):
        print(f"O arquivo {event.src_path} foi modificado")
    def on_moved(self, event):
        print(f"O arquivo {event.src_path} foi movido")

event_handler = fileEventHandler()
 
observer = Observer()

observer.schedule(event_handler, origin, recursive=True)

observer.start()

try:
    while True:
        time.sleep(2)
        print("Executando...")
except KeyboardInterrupt:
    print("Execução interrompida")
    observer.stop() 