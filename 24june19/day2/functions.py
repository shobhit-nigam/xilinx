#!/usr/bin/env python
# coding: utf-8

# In[1]:


#functions


# In[2]:


def funca():
    print("tuesday")
    print("wednesday")


# In[3]:


funca()


# In[4]:


varx = funca()


# In[5]:


type(varx)


# In[6]:


def funca():
    print("tuesday")
    print("wednesday")


# In[7]:


funcb = funca


# In[8]:


funcb()


# In[9]:


def funca():
    print("tuesday")
    print("wednesday")
    return 55.67


# In[10]:


varx = funca()


# In[11]:


type(varx)


# In[12]:


def funca():
    print("tuesday")
    print("wednesday")
    return 62, [6,7], 89


# In[13]:


vara, varb , varc = funca()


# In[14]:


type(varb)


# In[15]:


varc


# In[16]:


type(varc)


# In[22]:


def funca():
    print("tuesday")
    print("wednesday")
#    print(ia)
#    print("hi"
    return 62, [6,7], 89


# In[19]:


varb


# In[20]:


varb[0]


# In[23]:


vara = funca()


# In[24]:


vara, varb = funca()


# In[25]:


vara = 5,6,7


# In[26]:


vara, varb = 5,5,7


# In[27]:


funca


# In[28]:


type(funca)


# In[29]:


def funcc():
    print("in funcC")
    #lots of code
    #
    #
    def funcd():
        print("in d")
    #
    def funce():
        print("in e")
    #
    return None


# In[30]:


funcc()


# In[31]:


def funcc():
    print("in funcC")
    #lots of code
    #
    #
    def funcd():
        print("in d")
    #
    #
    funcd() #
    print("still in funcC")    
    return None


# In[32]:


funcc()


# In[33]:


funcd()


# In[34]:


def funcc():
    """ this is a specail function
    actualy function within function
    like inception"""
    print("in funcC")
    #lots of code
    #
    #
    def funcd():
        print("in d")
    #
    #
    funcd() #
    print("still in funcC")    
    return None


# In[35]:


help(funcc)


# In[36]:


def funcf():
    "small function"
    pass


# In[37]:


help(funcf)


# In[38]:


# __doc__ 


# In[39]:


funcf.__doc__


# In[ ]:




