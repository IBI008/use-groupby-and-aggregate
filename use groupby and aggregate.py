#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Import Pandas
import pandas as pd

# Load the excel data using read.
movies = pd.read_excel('movies_merge.xlsx')

# Load the csv file data using read.
ott = pd.read_csv('ott_merge.csv')

print(movies.columns)
print(movies.shape)
print(ott.columns)
print(ott.shape)


# In[3]:


# Merge the two DataFrames.
mov_ott = pd.merge(movies, ott, how='left', on='ID')

# View the DataFrame.
print(mov_ott.columns)
print(mov_ott.shape)


# In[5]:


mov_ott.head()


# In[29]:


# How many movies from each year were watched on Netflix since 2012?
mo_gby = mov_ott.groupby(['Year'])['Netflix'].agg('sum').reset_index()
# View the DataFrame
mo_gby[mo_gby['Year']>=2012]


# In[23]:


# What is the average run time of moviesreleased each year?

mo_gby1 = mov_ott.groupby(['Year'])['Runtime'].agg('mean').reset_index()
# View the DataFrame
mo_gby1[mo_gby1['Year']>=2012]


# In[34]:


# What are the best and the worst reviews that movies received on Rotten Tomatoes?
mo_gby2 = mov_ott.groupby(['Year'])['Rotten Tomatoes'].agg(['min','max']).reset_index()

# view the DataFrame.
mo_gby2[mo_gby2['Year']>=2012]


# In[ ]:




