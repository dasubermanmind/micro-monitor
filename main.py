import micomonitor as MM
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import sys

if __name__ == 'main':
    src_path = sys.argv[1]
    
    event_handler=MM()
    observer = Observer()
    observer.schedule(event_handler, path=src_path, recursive=True)
    print("Monitoring started")
    observer.start()
    try:
        while(True):
           time.sleep(1)
           
    except KeyboardInterrupt:
            observer.stop()
            observer.join()

