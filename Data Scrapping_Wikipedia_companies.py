#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests


# In[3]:


url='https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'
page=requests.get(url)
soup=BeautifulSoup(page.text,'html')


# In[5]:


print(soup)


# In[7]:


soup.find('table')


# In[9]:


soup.find_all('table')[1]


# In[12]:


soup.find('table',class_='wikitable sortable')


# In[13]:


table=soup.find_all('table')[1]


# In[14]:


print(table)


# In[23]:


world_titles=table.find_all('th')


# In[18]:


world_titles


# In[24]:


world_tables_titles=[title.text.strip() for title in world_titles]
print(world_tables_titles)


# In[25]:


import pandas as pd


# In[48]:


df=pd.DataFrame(columns=world_tables_titles)


# In[49]:


column_data=table.find_all('tr')


# In[51]:


for row in column_data[1:]:
    row_data=row.find_all('td')
    individual_row_data=[data.text.strip() for data in row_data]
    length=len(df)
    df.loc[length]=individual_row_data


# In[52]:


df


# In[54]:


df.to_csv(r'C:\Users\Deepika S\OneDrive\Desktop\DA Portfolio projects\Companies.csv',index=False)


# In[ ]:




