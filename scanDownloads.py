import sys
import time
import logging
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from watchdog.events import FileMovedEvent
from watchdog.events import FileCreatedEvent

class AdeorsFileSystemEventHandler(FileSystemEventHandler):

    def scanForViruses(self, event):
        if isinstance(event, FileMovedEvent):
            print ("File Downloaded!")
            print ("begin virus-check ....")
            subprocess.call(['clamscan', '--move=/home/adeor/Infected', event.dest_path])
            print ("virus-check finished!")
        else:
            print ("File Downloaded!")
            print ("begin virus-check ....")
            subprocess.call(['clamscan', '--move=/home/adeor/Infected', event.src_path])
            print ("virus-check finished!")

    def on_created(self, event):
        if isinstance(event, FileCreatedEvent):
            self.scanForViruses(event)

    def on_moved(self, event):
        if isinstance(event, FileMovedEvent):
            if event.dest_path+'.part' == event.src_path:
                self.scanForViruses(event)


if __name__ == "__main__":
    path = '/home/adeor/Downloads'
    event_handler = AdeorsFileSystemEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
