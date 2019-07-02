#!/usr/bin/env python
# coding: utf-8

# In[5]:


class shiva:
    powera = 'destroy'
    powerb = 'boons'
    __powerc = 'third eye'
    def natraja(self):
        print('dancing away ')


# In[6]:


class ganesha(shiva):
    powerd = 'takes away trouble'
    def eat(self):
        print('loves eating modaks')


# In[7]:


obja = ganesha()


# In[8]:


obja.natraja()


# In[9]:


varx = 67

varx = 66


# In[10]:


obja = shiva()


# In[12]:


class shiva:
    def __init__(self):
        print('in init of shiva')
    powera = 'destroy'
    powerb = 'boons'
    __powerc = 'third eye'
    def natraja(self):
        print('dancing away ')

class ganesha(shiva):
    powerd = 'takes away trouble'
    def eat(self):
        print('loves eating modaks')


# In[13]:


objg = ganesha()


# In[14]:


class shiva:
    def __init__(self):
        print('in init of shiva')
    powera = 'destroy'
    powerb = 'boons'
    __powerc = 'third eye'
    def natraja(self):
        print('dancing away ')

class ganesha(shiva):
    powerd = 'takes away trouble'
    powera = 'sleeping'
    def eat(self):
        print('loves eating modaks')


# In[15]:


objg = ganesha()


# In[16]:


objg.powera


# In[17]:


objs = shiva()
objs.powera


# In[18]:


class shiva:
    def __init__(self):
        print('in init of shiva')
    powera = 'destroy'
    powerb = 'boons'
    __powerc = 'third eye'
    def natraja(self):
        print('dancing away ')

class ganesha(shiva):
    def __init__(self):
        print('in init of ganesha')
    powerd = 'takes away trouble'
    powera = 'sleeping'
    def eat(self):
        print('loves eating modaks')


# In[19]:


objg = ganesha()


# In[22]:


pass


# In[40]:


class shiva:
    def __init__(self):
        print('in init of shiva')
    powera = 'destroy'
    powerb = 'boons'
#    __powerc = 'third eye'
    def natraja(self):
        print('dancing away ')

class ganesha(shiva):
    def __init__(self):
        super().__init__()
        print('in init of ganesha')
    powerd = 'takes away trouble'
    powera = 'sleeping'
    def eat(self):
        print('loves eating modaks')


# In[41]:


objg = ganesha()


# In[43]:


class shiva:
    def __init__(self):
        print('in init of shiva')
    powera = 'destroy'
    powerb = 'boons'
#    __powerc = 'third eye'
    def natraja(self):
        print('dancing away ')

class parvati:
    powerp = 'goddess of love'
    def __init__(self):
        print('in init of parvati')
        
class ganesha(parvati, shiva):
    def __init__(self):
        super().__init__()
        print('in init of ganesha')
    powerd = 'takes away trouble'
    powera = 'sleeping'
    def eat(self):
        print('loves eating modaks')


# In[45]:


objg = ganesha()


# In[57]:


class shiva:
    def __init__(self):
        print('in init of shiva')
    powera = 'destroy'
    powerb = 'boons'
#    __powerc = 'third eye'
    def natraja(self):
        print('shiva dancing away ')

class parvati:
    powerp = 'goddess of love'
    powerb = 'victory'
    def __init__(self):
        print('in init of parvati')
        
class ganesha(shiva, parvati):
    def __init__(self):
        super().__init__()
        print('in init of ganesha')
    powerd = 'takes away trouble'
    powera = 'sleeping'
    def eat(self):
        print('loves eating modaks')
    def natraja(self):
        print('ganesha dancing away ')
        super().natraja()


# In[58]:


objg = ganesha()


# In[59]:


objg.natraja()


# In[ ]:




