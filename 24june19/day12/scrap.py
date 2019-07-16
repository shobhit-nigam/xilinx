#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests


# In[2]:


requests.get('https://www.oreilly.com/free/')


# In[3]:


result = requests.get('https://www.oreilly.com/free/')


# In[4]:


result.headers


# In[5]:


type(result.headers)


# In[6]:


result.content


# In[7]:


from bs4 import BeautifulSoup


# In[8]:


result.text


# In[9]:


import requests
from bs4 import BeautifulSoup
result = requests.get('https://www.oreilly.com/free/')
data = result.text
soup = BeautifulSoup(data)


# In[10]:


soup


# In[11]:


for link in soup.find_all('a'):
    print(link.get('href'))


# In[14]:


import requests
from bs4 import BeautifulSoup
result = requests.get('https://www.xilinx.com/')
data = result.text
soup = BeautifulSoup(data)

for link in soup.find_all('a'):
    print(link.get('href'))


# In[15]:


import requests
from bs4 import BeautifulSoup
result = requests.get('https://www.oreilly.com/free/')
data = result.text
soup = BeautifulSoup(data)

samples = soup.find_all('a', 'item-title')


# In[17]:


print(samples)


# In[18]:


import requests
from bs4 import BeautifulSoup
result = requests.get('https://www.oreilly.com/free/')
data = result.text
soup = BeautifulSoup(data)

samples = soup.find_all('a', 'item-title')

data = {}

for book in samples:
    title = book.string.strip()
    data[title] = book.attrs['href']


# In[20]:


lista = list(data.keys())


# In[21]:


lista


# In[22]:


data['Machine Learning in Java']


# In[23]:


len(lista)


# In[ ]:




