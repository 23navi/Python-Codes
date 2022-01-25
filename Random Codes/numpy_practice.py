#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""
1. Create an array of 6 zeros
2. Create an array of 6 ones 
3.Create an array of 6 fives
4. Create an array of integers from 1 to 99
5. Create an array of all the odd integers ranging from 1 to 99
6. Create a 2X2 matrix filled with values from 1 to 4
7. Create a 3X3 matrix filled with values from 9 to 17
8. Make an indentity matrix of 4X4
9. With the help of NumPy generate a random nos in between 0 to 1
10. Create 10 points that are space linearly from each.
"""


# In[2]:


import numpy as np
import pandas as pd


# In[3]:


#1 
np.zeros(6)


# In[4]:


#2
np.ones(6)


# In[29]:


#3
#np.full((1,6), 6)

np.ones(6)*6


# In[7]:


#4
np.arange(1,100,1)


# In[8]:


#5
np.arange(1,100,2)


# In[12]:


#6 
np.arange(4).reshape(2,2)


# In[14]:


#6
np.arange(9,18,1).reshape(3,3)


# In[15]:


np.eye(4)


# In[18]:


np.random.random()


# In[22]:


np.linspace(0,9,10)


# In[ ]:




