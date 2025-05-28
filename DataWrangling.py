#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


df=pd.read_csv("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/dataset_part_1.csv")
df.head(10)


# In[3]:


df.isnull().sum()/len(df)*100


# In[4]:


df.dtypes


# In[5]:


df['LaunchSite'].value_counts()


# In[6]:


# Apply value_counts on Orbit column
df['Orbit'].value_counts()


# In[7]:


landing_outcomes=df['Outcome'].value_counts()
landing_outcomes


# In[8]:


for i,outcome in enumerate(landing_outcomes.keys()):
    print(i,outcome)


# In[9]:


bad_outcomes=set(landing_outcomes.keys()[[1,3,5,6,7]])
bad_outcomes


# In[11]:


landing_class=[0 if outcome in bad_outcomes else 1 for outcome in df['Outcome']]


# In[12]:


df['Class']=landing_class
df[['Class']].head(8)


# In[14]:


df.head()


# In[15]:


df["Class"].mean()


# In[ ]:




