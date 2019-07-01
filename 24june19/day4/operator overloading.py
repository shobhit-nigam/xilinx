#!/usr/bin/env python
# coding: utf-8

# In[1]:


class study:
    hours = 0
    minutes = 0
    def __init__(self, h, m):
        self.hours = h
        self.minutes = m


# In[2]:


prebreak = study(1, 30)


# In[3]:


postbreak = study(1, 40)


# In[4]:


total = study(0,0)


# In[5]:


total = prebreak + postbreak 
# study.__add__(prebreak, postbreak)


# In[22]:


class study:
    hours = 0
    minutes = 0
    def __init__(self, h=0, m=0):
        self.hours = h
        self.minutes = m
    def __add__(self, self2):       #magic function for +
        objc = study()
        min1 = self.hours * 60 + self.minutes
        min2 = self2.hours * 60 + self2.minutes
        mintotal = min1 + min2
        objc.hours = mintotal//60
        objc.minutes = mintotal%60
        return objc
    def display(self):
        print('we studied for ' , self.hours, ' hours and ', self.minutes, ' minutes')


# In[23]:


prebreak = study(1, 30)
postbreak = study(1, 40)
total = study(0,0)


# In[24]:


total = prebreak + postbreak


# In[25]:


total.display()


# In[26]:


total.hours


# In[27]:


4 + 5


# In[30]:


total = prebreak + postbreak


# In[31]:


class study:
    hours = 0
    minutes = 0
    def __init__(self, h=0, m=0):
        self.hours = h
        self.minutes = m
    def __add__(self, self2):       #magic function for +
        objc = study()
        min1 = self.hours * 60 + self.minutes
        min2 = self2.hours * 60 + self2.minutes
        mintotal = min1 + min2
        objc.hours = mintotal//60
        objc.minutes = mintotal%60
        return objc
    def __add__(self, min2):       #magic function for +
        objc = study()
        min1 = self.hours * 60 + self.minutes
        mintotal = min1 + min2
        objc.hours = mintotal//60
        objc.minutes = mintotal%60
        return objc
    def display(self):
        print('we studied for ' , self.hours, ' hours and ', self.minutes, ' minutes')


# In[32]:


prebreak = study(1, 30)
postbreak = study(1, 40)
total = study(0,0)


# In[33]:


total = prebreak + 20


# In[34]:


total.display()


# In[35]:


total = prebreak + postbreak


# In[ ]:




