import watchdog.events 
import watchdog.observers 
import time 
import click


@click.command()
@click.option('--date', default=1, help='Sort files into date subfolders')
@click.option('--name', prompt='Sort files into data type folders',
              help='The person to greet.')
def sort_files(count, name):
    """Sort files into corresponding subfolders based on selected option"""
    pass


@click.command()
@click.option('--date', default=1, help='Put incoming files into date subfolders')
@click.option('--name', prompt='Put incoming files into data type subfolders',
              help='The person to greet.')
def monitor_folder(count, name):
    """Monitor a folder and sort incoming files into corresponding subfolders based on selected option"""
    pass


class Handler(watchdog.events.PatternMatchingEventHandler): 
    def __init__(self): 
        # Set the patterns for PatternMatchingEventHandler 
        watchdog.events.PatternMatchingEventHandler.__init__(self, patterns=['*.csv'], ignore_directories=True, case_sensitive=False) 
  
    def on_created(self, event): 
        print("Watchdog received created event - % s." % event.src_path) 
        # Event is created, you can process it now 
  
    def on_modified(self, event): 
        pass #print("Watchdog received modified event - % s." % event.src_path) 
  
if __name__ == "__main__":
    src_path = "./data/"
    event_handler = Handler()
    observer = watchdog.observers.Observer()
    observer.schedule(event_handler, path=src_path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

