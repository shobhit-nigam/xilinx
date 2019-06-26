#!/usr/bin/env python
# coding: utf-8

# In[1]:


vara = 'xilinx'
i = 0
while i < 5:
    print(vara[i])
    i = i+1


# In[2]:


vara = 'xilinx'
i = 0
while i < len(vara):
    print(vara[i])
    i = i+1


# In[4]:


varu = 30
varv = 40

if varu == 20:
    print("its 20")
elif varu < 30:
    print("less than 30")
else:
    print("value is different")
    print("another line")
print("outside if-else")


# In[5]:


lista = ['gomes', 'janakiram', 'vinay', 'zahir', 'praveen', 'vineet']


# In[6]:


for name in lista:
    print(name)


# In[7]:


name


# In[8]:


for name in lista[2:]:
    print(name)


# In[10]:


for name in lista:
    print(name,len(name))


# In[11]:


for i in range(5):
    print(lista[i])


# In[12]:


for i in range(5):
    type(i)


# In[13]:


type(range(5))


# In[14]:


for i in range(lista[4]):
    print(i)


# In[15]:


for i in range(3,8):
    print(i)


# In[16]:


for i in range(3,11,2):
    print(i)


# In[18]:


for i in range(-1,-10,-3):
    varf = 30
    print(i)


# In[19]:


varf


# In[20]:


pass 


# In[21]:


for i in range(0,3):
    for j in range(0,3):
        if(i==j):
            print("tea/coffee/milk/ and everything else break")
            break
        else:
            print("no tea break")


# In[ ]:




