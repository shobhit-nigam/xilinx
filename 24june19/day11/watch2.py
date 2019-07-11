import sys
import os
import time 

class Stalker(object):
    run = True
    frequency = 1
    
    def __init__(self, filename, func_change, *args, **kwargs):
        self.filename = filename
        self.cache_stamp = 0
        self.func_change = func_change
        self.args = args
        self.kwargs = kwargs
        
    def look(self):
        cur_stamp = os.stat(self.filename).st_mtime
        if cur_stamp != self.cache_stamp:
            self.cache_stamp = cur_stamp
            #file has changed
            #print("fils has been modified")
            if self.func_change is not None:
                self.func_change(*self.args, **self.kwargs)
    
    def watch(self):
        while self.run:
            try:
                #observe changes
                time.sleep(self.frequency)
                self.look()
            except KeyboardInterrupt:
                print('exiting now')
                break
            except FileNotFoundError:
                #no action
                pass
            except:
                print('some strange error: %s' %sys.exc_info()[0])

def actiona(text):
    print(text)

def actionb(filename):
    print('we will log this file')
    #code for updating log file

filename = 'sample.txt'
#stalk_obj = Stalker(filename)
stalk_obj = Stalker(filename, actiona, text='its modified')
