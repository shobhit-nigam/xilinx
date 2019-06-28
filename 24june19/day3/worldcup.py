#!/usr/bin/env python
# coding: utf-8

# In[1]:


def funca(vara, varb):
    print("vara = ", vara)
    print("varb = ", varb)


# In[2]:


funca(6,8)


# In[3]:


def funca(vara = 45, varb = 23):
    print("vara = ", vara)
    print("varb = ", varb)


# In[4]:


funca(6,8)


# In[5]:


funca(6)


# In[11]:


def funca(vara , varc, varb):
    "please pass vara, varc, varb in that order"
    print("vara = ", vara)
    print("varb = ", varb)
    print("varc = ", varc)


# In[10]:


funca(vara=33, varb=55, varc=66)


# In[12]:


help(funca)


# In[13]:


def funca(vara , varc=22, varb=44):
    "please pass vara, varc, varb in that order"
    print("vara = ", vara)
    print("varb = ", varb)
    print("varc = ", varc)


# In[14]:


funca(45, vara=33)


# In[15]:


#default values
#positional arguments


# In[20]:


def funcb(*args):
    for val in args:
        print(val)


# In[17]:


funcb(4,5)


# In[18]:


funcb(5, 'h', "new", [7,8,9])


# In[27]:


def funcc(*args):
    for i in range(4):
        print(args[i])


# In[28]:


funcc(12 , 'h', "new", [7,8,9])


# In[23]:


import this


# In[24]:


def funcd(arg1, *args):
    for i in range(3):
        print(args[i])


# In[26]:


funcd(6, 8, 9, 13)


# In[29]:


#keyword arguments
def funce(**kwargs):
    for i in range(3):
        print(args[i])


# In[30]:


listb = [8, 9, 8, 7, 3, 2]


# In[32]:


listb.count()


# In[33]:


listc = (8, 9, 8, 7, 3, 2)


# In[34]:


#tuple


# In[35]:


tup1 = 9, 4, "str", 5


# In[36]:


type(tup1)


# In[37]:


tup2 = ((3,4), (7,8))


# In[38]:


tup2[0][0]


# In[42]:


tup1 = 9, 4, "str", '' ,5


# In[40]:


len(tup1)


# In[47]:


tup3 = (6, 7, listb)


# In[48]:


tup3[2] = 77


# In[49]:


listb


# In[50]:


tup3


# In[51]:


listb.append(5)


# In[52]:


listb


# In[53]:


tup3


# In[55]:


vary = (12/6)/2


# In[56]:


vary = (3)


# In[57]:


type(vary)


# In[58]:


vary = (3,)


# In[59]:


type(vary)


# 

# In[60]:


vary = 3,


# In[61]:


dictb = {'dhoni':'csk', 'warner':'srh', 'sharmaji':'mi'}


# In[62]:


dictb['dhoni']


# In[63]:


dictb.items()


# In[64]:


help(dictb.items)


# In[67]:


liste = list(dictb.keys())


# In[ ]:





# In[68]:


liste


# In[69]:


type(dictb.keys())


# In[71]:


dictb[liste[0]]


# In[72]:


dictb


# In[73]:


dictb[1]


# In[74]:


cricket = {'wc':'england', 10:'sachin', 7:'dhoni', 'ipl':dictb}


# In[75]:


dictb['rr'] = 'rahane'


# In[76]:


dictb


# In[77]:


dictb['dhoni'] = 'rps'


# In[78]:


dictb


# In[79]:


cricket


# In[80]:


cricket['ipl']['warner'][1]


# In[81]:


help(dict.get)


# In[84]:


dictb.get('dhoni')


# In[85]:


help(dict)


# In[87]:


def funck(**kwargs):
    for key, val in kwargs.items():
        print(val)
    pass


# In[88]:


funck(name="rahul", second = 'u', building = 'dtp')


# In[91]:


def funcj(varx,*args, **kwargs):
    for key, val in kwargs.items():
        print(val)
    pass


# In[93]:


funcj(varx=34, 66, 12, 78, name="rahul", second = 'u', building = 'dtp')


# In[95]:


get_ipython().run_line_magic('lsmagic', '')


# In[ ]:




