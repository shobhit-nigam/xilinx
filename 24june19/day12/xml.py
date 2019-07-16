#!/usr/bin/env python
# coding: utf-8

# In[1]:


import xml.etree.ElementTree as ET


# In[3]:


tree = ET.parse('sam.xml')


# In[4]:


root = tree.getroot()


# In[5]:


root


# In[6]:


root.tag


# In[7]:


root.attrib


# In[10]:


for child in root:
    print(child.tag, child.attrib)
    print(type(child))


# In[11]:


for var in root.iter('book'):
    print(var.attrib)


# In[13]:


import xml.etree.ElementTree as ET
tree = ET.parse('sam.xml')
root = tree.getroot()

for book in root.findall("./book/[price='5.95']"):
    print(book.attrib)
    


# In[14]:


import xml.etree.ElementTree as ET
tree = ET.parse('sam.xml')
root = tree.getroot()

for book in root.findall("./book/[price='5.95']"):
    print(book.)


# In[19]:


book.getchildren()[0].value


# In[20]:


x = book.getchildren()[0]


# In[21]:


x.text


# In[23]:


import xml.etree.ElementTree as ET
tree = ET.parse('sam.xml')
root = tree.getroot()

for book in root.findall("book"):
    for element in book:
        ele_auth = element.tag
        ele_val = book.find(ele)
        print(author)


# In[ ]:




