#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""
type()
print()
len()
sum()
min()
max()
sorted()
reversed()
count()

"""


# In[2]:


#abs()
inta = -2
print(abs(inta))


# In[3]:


4**3


# In[4]:


4**-3


# In[5]:


#all()
lista = [7,8,2,None]


# In[6]:


all(lista)


# In[7]:


help(any)


# In[8]:


bin(6)


# In[12]:


test = [1]
testb = 0.0
testc = -3
bool(testc)


# In[13]:


num = dict(x=10, y = 3)


# In[14]:


type(num)


# In[16]:


num['x']


# In[17]:


lista = ['mon', 'tue', 'wed']
listb = ['jul1', 'jul2', 'jul3']


# In[18]:


x = zip(lista, listb)


# In[19]:


type(x)


# In[20]:


x


# In[21]:


print(x)


# In[23]:


dicta = dict(zip(lista, listb))


# In[24]:


dicta


# In[25]:


help(zip)


# In[26]:


liste = []

for var in 'marvel' :
    liste.append(var)


# In[27]:


liste


# In[30]:


listf = [var          for var in 'friends']


# In[31]:


print(listf)


# In[34]:


list_n = [x for x in range(20) if x%3 == 0 and x%2 == 0]


# In[35]:


print(list_n)


# In[40]:



listg = [1, 2, 6, 7]
listh = [4,7,2,9]


# In[43]:


common = []


# In[44]:


for i in listg:
    for j in listh:
        if i == j:
            common.append(i)


# In[45]:


common 


# In[46]:


common = [i for i in listg for j in listh if i ==j]


# In[47]:


common


# In[50]:


def square_for(arr):
    result = []
    for i in arr:
        result.append(i**2)
    return result

get_ipython().run_line_magic('timeit', 'square_for(range(1,11))')


# In[51]:


def square_c(arr):
    return [i**2 for i in arr]

get_ipython().run_line_magic('timeit', 'square_c(range(1,11))')


# In[52]:


#split()


# In[53]:


text = " india vs bangladesh "


# In[54]:


listw = text.split()


# In[55]:


type(listw)


# In[56]:


listw


# In[57]:


text = "pak, ban, eng, nz, ind"


# In[60]:


listw = text.split(', ')


# In[61]:


listw


# In[62]:


listx = text.split(', ', 2)


# In[63]:


listx


# In[ ]:




