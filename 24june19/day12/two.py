#!/usr/bin/env python
# coding: utf-8

# In[2]:


from matplotlib import pyplot as plt
import numpy as np
x = np.arange(1,5)
y = x*3


# In[3]:


x


# In[4]:


y


# In[9]:


from matplotlib import pyplot as plt
import numpy as np
xa = [1,2,3,4]
ya = [1,4,9, 16]
x = np.arange(1,5)
y = x*3
plt.plot(xa,ya,'go', x,y, 'b^')
plt.show()


# In[15]:


from matplotlib import pyplot as plt
import numpy as np
xa = [1,2,3,4]
ya = [1,4,9, 16]
x = np.arange(1,5)
y = x*3
plt.plot(xa,ya,'g', x,y, 'b>')
plt.show()


# In[17]:


from matplotlib import pyplot as plt
import numpy as np
xa = [1,2,3,4]
ya = [1,4,9, 16]
x = np.arange(1,5)
y = x*3

########
plt.subplot(1,2,1)
plt.plot(xa,ya, 'go')
plt.title('first')

#######
plt.subplot(1,2,2)
plt.plot(x,y)
plt.title('first')


plt.show()


# In[23]:


from matplotlib import pyplot as plt
import numpy as np
xa = [1,2,3,4]
ya = [1,4,9, 16]
x = np.arange(1,5)
y = x*3

########
fig,ax = plt.subplots(nrows=2, ncols=2, figsize=(7,7))
ax[0,1].plot(xa,ya, 'go')
ax[0,1].set_title('first')


#######
ax[1,0].plot(x,y)
ax[1,0].set_title('first')


plt.show()


# In[26]:


from matplotlib import pyplot as plt
import numpy as np
xa = [1,2,3,4]
ya = [1,4,9, 16]
x = np.arange(1,5)
y = x*3

########
plt.subplot(2,2,1)
plt.plot(xa,ya, 'go')
plt.title('first')

#######
plt.subplot(2,2,4)
plt.plot(x,y)
plt.title('first')


plt.show()


# In[27]:


type(fig)


# In[30]:


fig.show()


# In[31]:


food = ['biryani', 'raita', 'salaan', 'thumsup', 'salad']
percentage = [65, 5, 10, 15, 5]


# In[32]:


plt.pie(percentage, labels=food)
plt.show()


# In[43]:


food = ['biryani', 'raita', 'salaan', 'thumsup', 'salad']
percentage = [65, 5, 10, 15, 5]
listb = [0, 0, 0, 0, 0]
plt.pie(percentage, labels=food, shadow=True, explode=listb, startangle=45)
plt.legend(title="Tejesh's lunch")
plt.axis('equal')
plt.show()


# In[47]:


from mpl_toolkits import mplot3d

height = np.array([60,70,49,65,55,80,66,46,59])
weight = np.array([86,87,69,63,54,83,76,86,69])

ax = plt.axes(projection = '3d')
ax.scatter3D(height, weight)

plt.show()


# In[ ]:




