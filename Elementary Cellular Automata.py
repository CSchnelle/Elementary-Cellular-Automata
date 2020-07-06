#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt


# In[2]:


num = 30


# In[3]:


output_pattern = [int(x)for x in np.binary_repr(num, width=8)]


# In[4]:


output_pattern


# In[5]:


input_pattern = np.zeros([8,3])
for i in range(8):
    input_pattern[i, :] = [int(x) for x in np.binary_repr(7-i, width=3)]


# In[6]:


input_pattern


# In[7]:


columns = 21
rows = int(columns/2)+1


# In[8]:


canvas = np.zeros([rows, columns+2])
canvas[0, int(columns/2)+1] = 1


# In[9]:


for i in np.arange(0, rows-1):
    for j in np.arange(0, columns):
        for k in range(8):
            if np.array_equal(input_pattern[k, :], canvas[i, j:j+3]):
                canvas[i+1, j+1] = output_pattern[k]


# In[10]:


plt.imshow(canvas[:, 1:columns+1], cmap='Greys', interpolation='nearest')
plt.title("Elementary Cellular Automata Rule {}".format(num))
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




