
# coding: utf-8

# In[2]:

import urllib2
from bs4 import BeautifulSoup
import pandas as pd

urls = ['https://en.wikipedia.org/wiki/List_of_musicals:_A_to_L',
        "https://en.wikipedia.org/wiki/List_of_musicals:_M_to_Z"]


# In[77]:

headers=[]
data_content=[]

def init(urls):
    for url in urls:
        make_soups_to_scrape(url)

def make_soups_to_scrape(this_url):
    page = urllib2.urlopen(this_url)
    soup = BeautifulSoup(page, "lxml")
    scrape_page_for_text(soup)

def get_text_fields(cells):
    for i in range(0, len(cells)):
        tmp = cells[i].find(text=True)
        if not tmp:
            tmp = '-'
        data_content[i].append(tmp)

def get_url(cells):
    tmp = cells[0].find('a')
    if not tmp: 
#        print 'tmp does not exist'
#        print tmp
        data_content[7].append('-')
    else:
#        print 'tmp exists'
#        print tmp
        url = tmp['href']
        if not url:
            url = '-'
        data_content[7].append(url)


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
                get_text_fields(cells)
                get_url(cells)
                

init(urls)


# In[78]:

df=pd.DataFrame()

for i in range(0, len(data_content)-1):
    df[headers[i]]=data_content[i]
df['url']=data_content[7]
##TODO: convert the url to a clickable version. Check whether the domain is necessary (there's a small number of exceptions) then add it

df


# In[60]:

print (len(data_content[7]))
print (len(data_content[6]))

print data_content[7]


# In[13]:

def get_musical_url():
    page = urllib2.urlopen('https://en.wikipedia.org/wiki/List_of_musicals:_A_to_L')
    soup = BeautifulSoup(page, "lxml")
    tables=soup.find_all('table', class_='wikitable sortable')          
    for table in tables:            
        for row in table.findAll("tr"):
            cells = row.findAll('td')
            #print len(cells)
            if len(cells) == 7:
                for a in cells[0].find_all('a', href=True):
                    print "Found the URL:", a['href']
get_musical_url()


# In[ ]:



