#!/usr/bin/env python
# coding: utf-8

# # Data Preparation

# In[106]:


import pandas as pd
import plotly.express as px #pip install plotly-express
import streamlit as st # pip install streamlit
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from tabulate import tabulate    # Used to create tables
from collections import Counter  # used to iterate or count occureneces of a value in a column


# In[107]:


st.set_page_config(page_title = "Los Angeles Crime Dashboard",
                  page_icon = "")


# In[108]:


df_all = pd.read_csv("H:\\Denis\\Data_Analysis_Training\\Python 2\\L.A Crime Analysis\\Los_Angeles_Crime.csv")


# In[110]:


df = df_all[["AREA_NAME","Type_of_Crime","VICTIM_AGE","VICTIM_SEX","Area_crime_conducted","WEAPON_DESC","STATUS_DESC"]]


# # Data Cleaning

# In[111]:


df.head()


# In[112]:


df.nunique()


# In[113]:


df.describe()


# In[114]:


df.info()


# In[115]:


df.count()


# In[116]:


df.isnull().sum()


# In[127]:


df = df.dropna()


# In[128]:


df.isnull().sum()


# In[129]:


df.info()


# In[130]:



#drop any rows that have 0 in the VICTIM_AGE column
df = df[df.VICTIM_AGE != 0]


# In[131]:


df.info()


# # Data Analysis

# ## IF AND Function

# In[31]:


# Checking the number of females on individuals more than 18 years
print(sum((df_clean.VICTIM_SEX  == "F") & (df_clean.VICTIM_AGE > 18)))


# In[32]:


# Checking the number of females on individuals below 18 years
print(sum((df_clean.VICTIM_SEX  == "F") & (df_clean.VICTIM_AGE < 18)))


# ## SUM IF Function

# In[33]:


print(df.groupby('STATUS_DESC').sum())


# In[45]:


xl = (df.groupby('STATUS_DESC')['VICTIM_AGE'].mean())
pd.DataFrame(xl)


# In[47]:


xm = (df.groupby('VICTIM_SEX')['VICTIM_AGE'].count())
pd.DataFrame(xm)


# In[54]:


# Average age of victims under the different gender specification
xn = (df.groupby('VICTIM_SEX')['VICTIM_AGE'].mean())
pd.DataFrame(xn)


# ## Mode (most occuring elements)

# In[56]:


# Area where most crimes occur
df.Area_crime_conducted.mode()


# In[71]:


# Getting the top 7 most common type of crime in LA
from collections import Counter  # used to iterate or count occureneces of a value in a column
words_to_count = (word for word in df.Type_of_Crime)
c = Counter(words_to_count)
xp = (c.most_common(8))
pd.DataFrame(xp) 


# In[93]:


# Top 10 most common type of crimes in L.A in percentage
counts_1 = df.Type_of_Crime.value_counts(normalize=True).mul(100).round(1).astype(str) + '%'
pd.DataFrame(counts_1.head(10))


# In[78]:



# Getting the top 7 specific areas where crime occurrs in LA
from collections import Counter  # used to iterate or count occureneces of a value in a column
words_to_count = (word for word in df.Area_crime_conducted)
c = Counter(words_to_count)
xp = (c.most_common(8))
pd.DataFrame(xp) 


# In[81]:


# Another method of getting the 10 areas where crimes occur in L.A
counts = df.Area_crime_conducted.value_counts()
pd.DataFrame(counts.head(10))


# In[91]:


# Adding percentage to the counts
counts = df.Area_crime_conducted.value_counts(normalize=True).mul(100).round(1).astype(str) + '%'
pd.DataFrame(counts.head(10))


# In[94]:



# Gender of victims in percentage
counts_gender = df.VICTIM_SEX.value_counts(normalize=True).mul(100).round(1).astype(str) + '%'
pd.DataFrame(counts_gender.head(10))


# In[132]:



# Most occuring age of the victims in percentage
counts_age = df.VICTIM_AGE.value_counts(normalize=True).mul(100).round(1).astype(str) + '%'
pd.DataFrame(counts_age.head(10))


# In[139]:


# Top ten locations with the highest crime reported
counts_area = df.AREA_NAME.value_counts(normalize=True).mul(100).round(1).astype(str) + '%'
pd.DataFrame(counts_area.head(10))


# In[ ]:




