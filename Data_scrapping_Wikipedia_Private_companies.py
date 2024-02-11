#!/usr/bin/env python
# coding: utf-8

# In[4]:


from bs4 import BeautifulSoup
import requests


# In[6]:


url='https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'
page=requests.get(url)
soup=BeautifulSoup(page.text,'html')


# In[7]:


print(soup)


# In[8]:


soup.find('table')


# In[9]:


soup.find_all('table')


# In[10]:


soup.find_all('table')[2:]


# In[17]:


soup.find_all('table',class_='wikitable sortable')[1:]


# In[31]:


table=soup.find_all('table')[2]


# In[32]:


print(table)


# In[36]:


world_private_titles=table.find_all('th')


# In[37]:


print(world_private_titles)


# In[38]:


world_titles=[title.text.strip() for title in world_private_titles]
print(world_titles)


# In[39]:


import pandas as pd


# In[41]:


df=pd.DataFrame(columns=world_titles)


# In[42]:


df


# In[46]:


column_data=table.find_all('tr')


# In[47]:


print(column_data)


# In[50]:


for row in column_data[1:]:
    row_data=row.find_all('td')
    print(row_data)
    ind_row_data=[data.text.strip() for data in row_data]
    length=len(df)
    df.loc[length]=ind_row_data


# In[51]:


df


# In[53]:


df.to_csv(r'C:\Users\Deepika S\OneDrive\Desktop\DA Portfolio projects\Private_companies.csv',index=False)


# In[ ]:




