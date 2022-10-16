from genericpath import isdir
import os
from watchdog.events import FileSystemEventHandler


# TODO: Research actions: 
# 1) Email
# 2) Push notifications (mobile) 
# 3) Upload to a server (Django/FastAPI) [ ]


def MicroMonitor(FileSystemEventHandler):

    def __init__(self):
        self.FILE_SIZE=1000
    
    
    # Define all the different actions that we want to monitor
    
    def on_created(self,event):
        pass
    
    def on_modified(self,event):
        pass
    
    def on_deleted(self,event):
        pass
    
    def size(self, filepath):
        if os.path.isdir(filepath):
            if os.path.getsize(filepath) > self.FILE_SIZE:
                pass