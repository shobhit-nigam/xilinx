#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json


# In[2]:


with open('example_2.json') as file:
    data = json.load(file)


# In[3]:


data


# In[4]:


type(data)


# In[5]:


print(json.dumps(data, indent = 2))


# In[7]:


pass


# In[8]:


data['quiz']['maths']['q1']['options'][2]


# In[9]:


#dict             object
#list, tuple      array
#str              string
#int, float       number
#True, False      true false
#None.            null


json
person = {'name':'gomes', 'age':26, 'children': 1, 'language':['python', 'irish', 'tamil', 'english']}

person_json = json.dumps(person)

print(person_json)


# In[10]:


json
person = {'name':'gomes', 'age':26, 'children': 1, 'language':['python', 'irish', 'tamil', 'english']}


with open('person.json', 'w') as json_file:
    json.dump(person, json_file)


# In[ ]:




