#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


#import data
G_temp = pd.read_csv('data/global_data.csv')
L_temp = pd.read_csv('data/city_data.csv')


# # global_temp

# In[3]:


G_temp.head()


# In[4]:


G_temp.tail()


# In[5]:


G_temp.info()


# In[6]:


#clean Global_temp
G_temp = G_temp.dropna().reset_index()


# In[7]:


G_temp.tail()


# In[8]:


G_temp = G_temp.drop([205,206],axis=0)


# In[9]:


#ploting
plt.plot(G_temp['year'],G_temp['avg_temp'])


# # City_temp

# In[10]:


L_temp.head()


# In[11]:


L_temp.tail()


# In[12]:


L_temp.info()


# In[13]:


#ploting
plt.plot(L_temp['year'],L_temp['avg_temp'])


# In[14]:


L_temp.count()


# In[15]:


#compare between local and global temp
x = G_temp['avg_temp'].rolling(2).mean()
y = L_temp['avg_temp'].rolling(10).mean()


# In[16]:


plt.plot(G_temp['year'],x,label='Global')
plt.plot(L_temp['year'],y,label='Cairo')
plt.legend()
plt.xlabel("Years")
plt.ylabel("Temperature (°C)") 
plt.title("Cairo City Average Temperature")
plt.show()


# In[ ]:





# In[ ]:




