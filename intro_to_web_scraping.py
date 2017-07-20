
# coding: utf-8

# In[1]:

import urllib2
from bs4 import BeautifulSoup
import pandas as pd

urls = ['https://en.wikipedia.org/wiki/List_of_musicals:_A_to_L',
        "https://en.wikipedia.org/wiki/List_of_musicals:_M_to_Z"]


# In[23]:

headers=[]
data_content=[]

def init(urls):
    for url in urls:
        make_soups_to_scrape(url)

def make_soups_to_scrape(this_url):
    page = urllib2.urlopen(this_url)
    soup = BeautifulSoup(page, "lxml")
    scrape_page_for_text(soup)

def scrape_page_for_text(thisSoup):
    #Generate lists
    tables=thisSoup.find_all('table', class_='wikitable sortable')
    
    for table in tables:

        if len(headers) == 0:
            for head in table.findAll("th"):
                if len(head) > 0:
                    headers.append(head.find(text=True))
                    data_content.append([])
            del headers[0]
            
        for row in table.findAll("tr"):
            cells = row.findAll('td')
            #print len(cells)
            if len(cells) == 7:
                for i in range(0, len(cells)):
                    tmp = cells[i].find(text=True)
                    if not tmp:
                        tmp = '-'
                    data_content[i].append(tmp)

init(urls)


# In[25]:

df=pd.DataFrame()

for i in range(0, 7):
    df[headers[i]]=data_content[i]

df


# In[ ]:



