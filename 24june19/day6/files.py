#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
os.getcwd()


# In[2]:


fptr = open('file1.txt', 'r')


# In[3]:


type(fptr)


# In[4]:


stra = fptr.read(4)


# In[5]:


print(stra)


# In[6]:


strb = fptr.readline()


# In[7]:


print(strb)


# In[8]:


fptr.close()


# In[9]:


fptr = open('file1.txt', 'r')
stra = fptr.read()


# In[10]:


stra


# In[11]:


fptr = open('file2.txt', 'w')


# In[12]:


fptr = open('file2.txt', 'w')


# In[13]:


#import os 
#os.chown()


# In[14]:


fptr.write("dinesh wants a holiday tomm")


# In[15]:


fptr.close()


# In[16]:


import os


# In[17]:


with open('file1.txt', 'r') as fptr:
    data = fptr.read()
    print(data)


# In[18]:


with open('file3.txt', 'w') as fptr:
    fptr.write('some hands, all hands')


# In[23]:


fptr = open('file2.txt', 'r')


# In[25]:


fptr.read(4)


# In[26]:


fptr.tell()


# In[22]:


fptr.close()


# In[27]:


fptr.seek(10)


# In[28]:


fptr.tell()


# In[29]:


fptr.read()


# In[ ]:




