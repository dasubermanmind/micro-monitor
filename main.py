import os
import sys
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


def MicroMonitor(FileSystemEventHandler):
    FILE_SIZE=1000
    
    
    # Define all the different actions that we want to monitor
    
    def on_created(self,event):
        pass
    
    def on_modified(self,event):
        pass
    
    def on_deleted(self,event):
        pass
    
    def size(self):
        pass



# TODO: Research actions: 
# 1) Email
# 2) Push notifications (mobile) 
# 3) Upload to a server (Django/FastAPI) [ ]










if __name__ == 'main':
    print('HELLO WORLD')

