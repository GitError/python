"""

high-level: sort incoming files into their folders based on the  metadata and execution flag
-d -- by date. folder name = yyy-mm-dd
-s -- by source/ origin. 

"""

import time
import sys
import datetime

from watchdog.events import PatternMatchingEventHandler
from watchdog.observers import Observer


def main(argv):    
    try:
        my_observer = Observer()
        my_observer.schedule(my_event_handler, path, recursive=go_recursively)
        my_observer.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            my_observer.stop()
            my_observer.join()
    except ValueError:
        pass


def get_file_details(src_path):
    print(src_path)
    pass


def on_created(event):
    print(f"{datetime.datetime.now()} log - {event.src_path} created!")


def on_deleted(event):
    print(f"{datetime.datetime.now()} log - {event.src_path} deleted")


def on_moved(event):
    print(f"{datetime.datetime.now()} moved from {event.src_path} to {event.dest_path}")


# called on every other event, skip
def on_modified(event):
    pass #print(f"{datetime.datetime.now()} log - {event.src_path} modified")


if __name__ == "__main__":
    patterns = "*"
    ignore_patterns = ""
    ignore_directories = False
    case_sensitive = True
    my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)
    my_event_handler.on_created = on_created
    my_event_handler.on_deleted = on_deleted
    my_event_handler.on_modified = on_modified
    my_event_handler.on_moved = on_moved
    path = "./data/"
    go_recursively = False
    main(sys.argv)

