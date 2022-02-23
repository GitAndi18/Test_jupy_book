#!/usr/bin/env python
# coding: utf-8

# # Hide test cell

# In[1]:


import numpy as np
import matplotlib.pyplot as plt

my_hidden_variable = 'wow'

# The variable for this is defined in the cell above!
print(my_hidden_variable)


# In[2]:


x = np.arange(500)
y = np.random.randn(500)

fig, ax = plt.subplots()
ax.scatter(x, y, c=y, s=x)


# In[ ]:





# In[ ]:




