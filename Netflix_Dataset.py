#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Import dataset
import pandas as pd
data = pd.read_csv(r"C:\Users\Mauricio Cantu\OneDrive\Documents\Datasets and Projects\Netflix_Python\Netflix_Dataset.csv")


# In[8]:


data.head()


# In[ ]:


#Get basic data information


# In[9]:


data.tail()


# In[12]:


data.shape


# In[15]:


data.size


# In[16]:


data.columns


# In[17]:


data.dtypes


# In[18]:


#Combine all of this information using ".info()"
data.info()


# ## Task .1. Are there any duplicates in the dataset? Remove if so.

# In[19]:


data.shape


# In[25]:


data[data.duplicated()]


# In[24]:


data.drop_duplicates(inplace = True)


# In[26]:


data.shape


# ## Task .2. Are there any Null Values? Use a heatmap to show them.

# In[27]:


data.isnull()


# In[28]:


data.isnull().sum()


# In[30]:


#Import Seaborn library for heatmap
import seaborn as sns


# In[31]:


sns.heatmap(data.isnull())


# ### Analysis Q1: What is the Show ID and Director for the show "House of Cards"?

# In[32]:


data.head()


# In[33]:


# We can use isin() function...
data[data["Title"].isin(["House of Cards"])]


# In[35]:


# We can also use str.contains() function
data[data["Title"].str.contains("House of Cards")]


# ### Analysis Q2. What was the year for the highest number of TV Shows and Movies released? Use a Bar Graph.

# In[36]:


# Add a column using to_datetime() function...
data.dtypes


# In[37]:


data['Date_N'] = pd.to_datetime(data['Release_Date'])


# In[38]:


data.head()


# In[40]:


data.dtypes


# In[43]:


data["Date_N"].dt.year.value_counts()


# In[44]:


data["Date_N"].dt.year.value_counts().plot(kind='bar')


# ### Analysis Q3. How many Movies and TV Shows are in the dataset?

# In[55]:


data.head(2)


# In[56]:


# Use groupby() function...
data.groupby("Category").Category.count()


# ### Analysis Q4. Show all the movies that were released in the year 2000.

# In[57]:


# Create a new column...
data['Year'] = data['Date_N'].dt.year


# In[58]:


data.head(2)


# In[64]:


data[(data['Category'] == 'Movie') & (data['Year'] == 2000)]


# ### Analysis Q5. Show only the titles of TV Shows released in Mexico only.

# In[66]:


data[(data['Category'] == 'TV Show') & (data['Country'] == 'Mexico')] ['Title']


# ### Analysis Q6. Show top 10 Directors, who have the most TV Shows and Movies in Netflix.

# In[68]:


data['Director'].value_counts().head(10)


# ### Analysis Q7. Show all the movies where (Category is Movie and Type is Comedies) or (Country is United Kingdom)

# In[72]:


data[ (data['Category'] == 'Movie') & (data['Type'] == 'Comedies') | (data['Country'] == 'United Kingdom')]


# ### Analysis Q8. In how many Movies/TV Shows Tom Cruise was casted?

# In[73]:


data[data['Cast'] == 'Tom Cruise']


# In[74]:


# You can also use str.contains() function...
data[data['Cast'].str.contains('Tom Cruise')]


# In[77]:


# Lets remove Null Values in Cast. First, we create a new dataframe
data_new = data.dropna()


# In[78]:


data_new.head(2)


# In[79]:


data_new[data_new['Cast'].str.contains('Tom Cruise')]


# ### Analysis Q9. What are the different Ratings defined by Netflix?

# In[81]:


data['Rating'].unique()


# In[83]:


data['Rating'].nunique()


# ### Analysis Q9.1 How many Movies got the 'TV-14' Rating in Canada

# In[87]:


data[(data_new['Category'] == 'Movie') & (data['Rating'] == 'TV-14') & (data['Country'] == 'Canada')].shape


# ### Analysis Q9.2 How many TV Shows have an 'R' Rating after 2018?

# In[93]:


data[(data['Category'] == 'TV Show') & (data['Rating']=='R') & (data['Year'] > 2018)]


# 
