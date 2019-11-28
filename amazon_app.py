# -*- coding:utf-8-*-

import pandas as pd

import requests
from bs4 import BeautifulSoup

URL = "https://www.amazon.com/s?k=economics&i=stripbooks&crid=1BL27K8UDGFRV&sprefix=economic%2Cstripbooks%2C209&ref=nb_sb_ss_i_1_8"

headers = {"User-Agent":'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}

page = requests.get(URL, headers=headers).text

soup = BeautifulSoup(page, 'lxml')

items = soup.find_all("div", {"class":"s-result-list s-search-results sg-row"})
link_list = list()
names = list()

for item in items:
    links = soup.find_all("a", {"class": "a-link-normal a-text-normal"})
    for link in links:
        link_list.append(link.get('href'))

    book_names = soup.find_all("span", {"class":"a-size-medium a-color-base a-text-normal"})    
    for name in book_names:

        name = ' '.join(name.string.split()) + '\n'
        names.append(name)

       

#convert book_names and link_list to dictionary
res = (dict(zip(names, link_list)))

#extract data using pandas
project_df = pd.DataFrame.from_dict(res, orient='index')

#manipulating the table
project_df['book_name'] = project_df.index
project_df.columns = ['book_url', 'book_name']
project_df = project_df.reset_index(drop=True)
#print(project_df.head())

#export dataframe as csv
project_df.to_csv('book_list.csv')    

     
    

