#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
import os


# In[2]:


import sys
import os
import time 

class Stalker(object):
    run = True
    frequency = 1
    
    def __init__(self, filename):
        self.filename = filename
        self.cache_stamp = 0
        
    def look(self):
        cur_stamp = os.stat(self.filename).st_mtime
        if cur_stamp != self.cache_stamp:
            self.cache_stamp = cur_stamp
            #file has changed
            print("fils has been modified")
    
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

filename = 'sample.txt'
stalk_obj = Stalker(filename)


# In[3]:


stalk_obj.watch()


# In[ ]:




