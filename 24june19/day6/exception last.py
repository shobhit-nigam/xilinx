#!/usr/bin/env python
# coding: utf-8

# In[3]:


def funca():
    try:
        print('testing some funca')
        raise ValueError('something wrong in value')
    except ValueError:
        print("name is wrong")


# In[2]:


funca()


# In[4]:


def funca():
    try:
        print('testing some funca')
        raise ValueError('something wrong in value')
    except NameError:
        print("name is wrong")


# In[5]:


funca()


# In[6]:


try:
    funca()
except :
    print('handled')


# In[7]:


import sys

try:
    funca()
except Exception as ex:
    print('handled')
    print('type of exception: {0} '.format(type(ex).__name__))
    print('type of exception: {0} '.format(ex.args))


# In[10]:


def funca():
    try:
        print('testing some funca')
        raise ValueError(5, 6)
    except NameError:
        print("name is wrong")


# In[15]:


try:
    funca()
except Exception as ex:
    print('handled')
    print('type of exception: {0} '.format(type(ex).__name__))
    print('type of exception: {} ' .format(ex.args))


# In[16]:


import sys


# In[17]:


try:
    funca()
except Exception as ex:
    print('handled')
    data = sys.exc_info()


# In[18]:


data


# In[25]:


try:
    funca()
except Exception as ex:
    print('handled')
    data = sys.exc_info()
    print(sys.exc_info()[0])
    print(type(sys.exc_info()[1]))
    print(sys.exc_info()[2].tb_lineno) 


# In[ ]:




