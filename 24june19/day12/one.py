#!/usr/bin/env python
# coding: utf-8

# In[1]:


from matplotlib import pyplot as plt 


# In[3]:


plt.plot([1,2,3], [3,5,2])
plt.show()


# In[5]:


from matplotlib import pyplot as plt 

x = [4,9,11]
y = [12, 15, 7]
plt.plot(x,y)

plt.title('first plot')
plt.ylabel('Y axis')
plt.xlabel('X axis')

plt.show()


# In[20]:


from matplotlib import pyplot as plt 
from matplotlib import style

#style.use('default')
style.use('ggplot')
x = [4,9,11]
y = [12, 15, 7]

x2 = [4, 10,11]
y2 = [6, 15, 8]

plt.plot(x,y, color='r', linewidth= 4)
plt.plot(x2,y2, color='g', linewidth = 4)

plt.title('first plot')
plt.ylabel('Y axis')
plt.xlabel('X axis')

plt.show()


# In[16]:


help(style.use)


# In[22]:


from matplotlib import pyplot as plt 
from matplotlib import style

#style.use('default')
style.use('ggplot')
x = [4,9,11]
y = [12, 15, 7]

x2 = [4, 10,11]
y2 = [6, 15, 8]

plt.plot(x,y, color='r', linewidth= 4, label = 'line one')
plt.plot(x2,y2, color='g', linewidth = 4, label = 'line two')

plt.legend()

plt.title('first plot')
plt.ylabel('Y axis')
plt.xlabel('X axis')

plt.show()


# In[23]:


help(plt.legend)


# In[24]:


from matplotlib import pyplot as plt 
from matplotlib import style

#style.use('default')
style.use('ggplot')
x = [4,9,11]
y = [12, 15, 7]

x2 = [4, 10,11]
y2 = [6, 15, 8]

plt.plot(x,y, color='r', linewidth= 4, label = 'line one')
plt.plot(x2,y2, color='g', linewidth = 4, label = 'line two')

plt.legend(loc = 10)

plt.title('first plot')
plt.ylabel('Y axis')
plt.xlabel('X axis')

plt.show()


# In[28]:


from matplotlib import pyplot as plt 
from matplotlib import style

#style.use('default')
style.use('ggplot')
x = [4,9,11]
y = [12, 15, 7]

x2 = [4, 10,11]
y2 = [6, 15, 8]

plt.bar(x,y, align = 'center')
#plt.bar(x2,y2, align = 'center')

#plt.legend()

plt.title('first bar plot')
plt.ylabel('Y axis')
plt.xlabel('X axis')

plt.show()


# In[30]:


y = [122,57,140, 1, 18, 102, 104, 103, 1]
x = [i for i in range(1,10)]

plt.bar(x,y, align='center')
#plt.plot(x,y)
plt.title('Sharma')
plt.ylabel('runs')
plt.xlabel('innings')

plt.show()


# In[32]:


y = [122,57,140, 1, 18, 102, 104, 103, 1]
x = [i for i in range(1,10)]
y2 = [73, 25, 0, 35, 0, 5, 20, 8, 1]
x2 = x
plt.bar(x,y, align='center')
plt.bar(x2,y2, align='center', color='g')
#plt.plot(x,y)
plt.title('Sharma')
plt.ylabel('runs')
plt.xlabel('innings')

plt.show()


# In[35]:


scores1 = [122,57,140, 1, 18, 102, 104, 103, 1]
scores2 = [73, 25, 0, 35, 0, 5, 20, 8, 1]
x = [i for i in range(1,10)]
x2 = x
y = []
y2 = []

total1=0
total2=0

for i in range(0,9):
    total1 = total1 + scores1[i]
    total2 = total2 + scores2[i]
    if i == 0:
        y.append(total1)
        y2.append(total2)
    else:
        y.append(total1//(i+1))
        y2.append(total2//(i+1))
    print(i+1, '\t', scores2[i], '\t', y2[i])



plt.plot(x,y)
plt.plot(x2,y2)
plt.title('averages')
plt.ylabel('avg runs')
plt.xlabel('innings')

plt.show()


# In[45]:


scores1 = [122,57,140, 1, 18, 102, 104, 103, 1]
scores2 = [73, 25, 0, 35, 0, 5, 20, 8, 1]
scores3 = {0:0, 40:1, 79:0, 106:0, 148:1, 41:1, 39:1, 27:1, 67:1}
scores4 = {34:1, 27:1, 1:1, 28:1, 56:0, 42:0, 35:1, 0:0, 50:1}
x = [i for i in range(1,10)]
x2 = x
x3 = x
x4 = x
y = []
y2 = []
y3 = []
y4 = []

total1=0
total2=0
total3=0
total4=0

for i in range(0,9):
    total1 = total1 + scores1[i]
    total2 = total2 + scores2[i]
    if i == 0:
        y.append(total1)
        y2.append(total2)
    else:
        y.append(total1//(i+1))
        y2.append(total2//(i+1))


i=0
deno = 1
for run, out in scores3.items():
    total3 = total3 + run
    if out == 0:
        deno = deno
        y3.append(total3//deno)
    else:
        y3.append(total3//deno)   
        deno = deno + 1
    i = i+1 

    
i=0
deno = 1
for run, out in scores4.items():
    total4 = total4 + run
    if out == 0:
        deno = deno
        y4.append(total4//deno)
    else:
        y4.append(total4//deno)   
        deno = deno + 1
    i = i+1 

y3[0] = None

plt.plot(x,y, color = 'red')
plt.plot(x2,y2, color = 'y')
plt.plot(x3,y3, color = 'black')
plt.plot(x4,y4, color = 'b')
plt.title('averages')
plt.ylabel('avg runs')
plt.xlabel('innings')

plt.show()


# In[ ]:




