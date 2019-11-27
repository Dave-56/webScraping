# -*- coding:utf-8-*-

import pandas as pd

from selenium import webdriver #allow launching browser
from selenium.webdriver.common.by import By # allow search with parameters
from selenium.webdriver.support.ui import WebDriverWait # allow waiting for page to load
from selenium.webdriver.support import expected_conditions as EC # determine whether the web page has loaded
from selenium.common.exceptions import TimeoutException # handling timeout situation

driver_option = webdriver.ChromeOptions()
driver_option.add_argument(" — incognito")
chromedriver_path = '/usr/local/bin/chromedriver'

def create_webdriver():
    return webdriver.Chrome(executable_path=chromedriver_path)


#open the webpage
browser = create_webdriver()
browser.get("https://github.com/collections/machine-learning")

#Extract all projects
projects = browser.find_elements_by_xpath("//h1[@class='h3 lh-condensed']")
#print(projects)  
 
project_list = dict()

#loop thru projects to get each text and link
for children in projects:
    children_name = children.text
    children_url = children.find_elements_by_xpath("a")[0].get_attribute('href')
    project_list[children_name] = children_url

#close connection
browser.quit()  

#extract data using pandas
project_df = pd.DataFrame.from_dict(project_list, orient='index')

#manipulating the table
project_df['project_name'] = project_df.index
project_df.columns = ['project_url', 'project_name']
project_df = project_df.reset_index(drop=True)
print(project_df.head())

#export dataframe as csv
project_df.to_csv('project_list.csv')    