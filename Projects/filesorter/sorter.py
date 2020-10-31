import os
import watchdog.events 
import watchdog.observers 
import time 
import click


@click.command()
@click.option('--monitor', default=0, help='Monitor and sort incoming files')
@click.option('--src-folder', default="./data/", help='Source folder')
@click.option('--dest-folder', default="./data/sorted/", help='Target folder')
@click.option('--sort-by', default=1, help='1- creation-date, 2- last-access-date, 3- data type')
def cli(monitor, src_folder, dest_folder, sort_by):
    make_folder(src_folder)
    make_folder(dest_folder)
    if(monitor == 0):
        print("--- sort & exit ---")
        with os.scandir(src_folder) as entries:
            for entry in entries:
                if entry.is_file():
                    print("processing:\t\t\t" + entry.name)
        print("--- done ---")
        exit()
    else:
        print("--- monitor incoming files ---")
        event_handler = Handler()
        observer = watchdog.observers.Observer()
        observer.schedule(event_handler, path=src_folder, recursive=True)
        observer.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
        observer.join()        
        print("--- done ---")


class Handler(watchdog.events.PatternMatchingEventHandler): 
    def __init__(self): 
        watchdog.events.PatternMatchingEventHandler.__init__(self, patterns=['*.csv'], ignore_directories=True, case_sensitive=False) 
  
    def on_created(self, event): 
        print("Watchdog received created event - % s." % event.src_path)

    def on_modified(self, event): 
        pass #print("Watchdog received modified event - % s." % event.src_path) 


def get_file_info(file_path):
    pass


def make_folder(src_path):
    if not os.path.exists(src_path):
        os.mkdir(src_path)


if __name__ == '__main__':
    cli()
