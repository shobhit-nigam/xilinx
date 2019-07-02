#!/usr/bin/env python
# coding: utf-8

# In[1]:


seta = {7,8,7,4,5,6}
setb = {1,2,7,4,3}


# In[2]:


print(seta)


# In[4]:


seta


# In[7]:


setc = seta | setb 


# In[8]:


setc


# In[9]:


type(setc)


# In[10]:


#exception handling
vara = 0
varb = 10


# In[12]:


varb/vara


# In[13]:


varb/var


# In[14]:


#try
#except


# In[15]:


vara = 0
varb = 10
try: 
    result = varb/vara
    print(reuslt)
    #unreachable
except ZeroDivisionError:
    print("divide by zero error")


# In[17]:


vara = 5
varb = 10
try: 
    result = varb/vara
    print(reuslt)
except ZeroDivisionError:
    print("divide by zero error")
except NameError:
    print('you have a typo')


# In[18]:


vara = 5
varb = 10
try: 
    result = varb/vara
    print(result)
except ZeroDivisionError:
    print("divide by zero error")
except NameError:
    print('you have a typo')


# In[23]:


lista = [5,7,8,9]
avg = 1
i = int(input('enter a num: '))
try:
    avg = sum(lista)/len(lista)
    print(avg)
    print(lista[i])
except ZeroDivisionError:
    print("divide by zero error")
except NameError:
    print('you have a typo')


# In[26]:


lista = [5,7,8,9]
avg = 1
i = int(input('enter a num: '))
try:
    avg = sum(lista)/len(lista)
    print(avg)
    print(lista[i])
except ZeroDivisionError:
    print("divide by zero error")
except NameError:
    print('you have a typo')
except :
    print('something went wrong')


# In[28]:


lista = [5,7,8,9]
try :
    i = int(input('enter a num: '))
    if i <= 0 :
        raise ValueError ("this is not  a positive value")
    else:
        print(lista[i])
except ValueError as VE:
    print(type(VE))
    print(VE)


# In[29]:


lista = [5,7,8,9]
try :
    i = int(input('enter a num: '))
    if i <= 0 :
        raise ValueError
    else:
        print(lista[i])
except ValueError as VE:
    print(type(VE))
    print(VE)


# In[35]:


def funca():
    try :
        pass
    except :
        pass
    return None


# In[36]:


try:
    funca()
except:
    pass


# In[37]:


class appError(Exception):
    "base class for application exceptions"
    pass


# In[39]:


class appError(Exception):
    "base class for application exceptions"
    pass

class ValueTooSmall(appError):
    "value is too small"
    pass

class ValueTooLarge(appError):
    "value is too large"
    pass
    
number = 10
while True:
    try :
        i_num = int(input("enter a number"))
        if i_num < number:
            raise ValueTooSmall
        elif i_num > number:
            raise ValueTooLarge
        break    
    except ValueTooSmall:
        print(ValueTooSmall.__doc__)
    except ValueTooLarge:
        print(ValueTooLarge.__doc__)
print('congrats, you guessed it write')        


# In[ ]:




