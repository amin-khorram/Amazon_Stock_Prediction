#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd
import requests
from bs4 import BeautifulSoup
get_ipython().system('pip install lxml==5.1.0')


# In[10]:


#take the url address from Yahoo finance "Amazon"
url_test= "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/amazon_data_webpage.html"
data = requests.get(url_test).text
print(data)


# In[11]:


soup = BeautifulSoup(data, 'lxml')


# In[19]:


amazon_data = pd.DataFrame(columns=["Date", "Open", "High", "Low", "Close", "Adj_Close", "Volume"])


# In[20]:


amazon_data = pd.DataFrame(columns=["Date", "Open", "High", "Low", "Close", "Adj_Close", "Volume"])

for row in soup.find("tbody").find_all("tr"):
    col = row.find_all("td")
    date = col[0].text
    Open = col[1].text
    high = col[2].text
    low = col[3].text
    close = col[4].text
    adj_close = col[5].text
    volume = col[6].text
    
    amazon_data = amazon_data.append({"Date":date, "Open":Open, "High":high, "Low":low, "Close":close, "Adj_Close":adj_close, "Volume":volume}, ignore_index=True)


# In[21]:


amazon_data.head(5)


# In[18]:




