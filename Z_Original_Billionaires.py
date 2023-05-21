# -*- coding: utf-8 -*-
"""
Created on Wed May 10 09:17:36 2023

@author: janhr
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

N = 100 


base_url =  

sites_to_visit = []    #empty list to store all sites to visit


def get_raw_richies(N: int): 
  ##loop through all the pages:
  for i in range(1,11):
  site equals     
  while site not empty"
      try" 
      site = f"{base_url}{i}{'/'}"
      sites_to_visit.append(site)

raw_richies ´get_raw

#print(sites_to_visit)



lst = [] #empty list to store links to all the sites of all the people

for url in sites_to_visit:
    ##send get request to urls and store the response:
    response = requests.get(url)
    
    ##create a beautifulsoup object from the content of the response:
    soup = BeautifulSoup(response.content, 'lxml')
    # TODO: persist data
    
    tr = soup.body.find('div', class_='w-content').find_all('a', class_='')
    
    
    prefix = 'https://www.therichest.com/'
    
    #print(tr)
    
    for a in tr:
        if a.has_attr('href'):
            
            link = a.get('href')
            
            lst.append(prefix + link)
#print(lst)
    
    
    
    #print(lst)



dictio = {} #empty dictionary to store all the variables to people



##get the values for all the variables:
for link in lst:
    a = requests.get(link)
    ppl = BeautifulSoup(a.content, 'lxml' )
    #print(ppl)
    
    
    
    
    
    
    if ppl.find('strong', class_ = 'net-profile_header_networth') != None:    
        
        net_worth = ppl.find('strong', class_ = 'net-profile_header_networth').get_text()
     
     #   print(net_worth)
        
        
        
        
        
        
        
        
        
        
        
        
        
        condition_0 = ppl.find('h3', text='Source of Wealth: ')
        
        if condition_0 != None:
            
            source_of_wealth = condition_0.next_sibling.next_sibling.get_text()
           
           # print(source_of_wealth)
        else: 
           source_of_wealth = 'Unknown'
          
          # print(source_of_wealth)
        
        
        
        
        
        
        
        condition_1 = ppl.find('h3', text='Age: ')
        
        if condition_1 != None:
            
            Age = condition_1.next_sibling.next_sibling.get_text()
        
        #    print(Age)
        else: 
           Age = 'Unknown'
       
       #    print(Age)
        
        
        
        
        
        condition_2 = ppl.find('h3', text='Birth Place: ')
        
        if condition_2 != None:
            
            Place = condition_2.next_sibling.next_sibling.get_text()
         
         #   print(Place)
        else: 
           Place = 'Unknown'
          
          # print(Place)
        
        
        
        
        
        
        condition_3 = ppl.find('h3', text='Marital Status: ')
        
        if condition_3 != None:
            
            Status = condition_3.next_sibling.next_sibling.get_text()
          
          #  print(Status)
        else: 
           Status = 'Unknown'
       
       #    print(Status)
        
        
        
        
        
        
        condition_4 = ppl.find('h3', text='Full Name: ')
        
        if condition_4 != None:
            
            Name = condition_4.next_sibling.next_sibling.get_text()
          
          #  print(Name)
        else: 
           Name = 'Unknown'
         
         #  print(Name)
        
        
        
        
        
        
        condition_5 = ppl.find('h3', text='Nationality: ')
        
        if condition_5 != None:
            
            Nationality = condition_5.next_sibling.next_sibling.get_text()
          
          #  print(Nationality)
        else: 
           Nationality = 'Unknown'
         
         #  print(Nationality)
        
        
        
        
        
        condition_6 = ppl.find('h3', text='Date of Birth: ')
        
        if condition_6 != None:
            
            Birth = condition_6.next_sibling.next_sibling.get_text()
         
         #   print(Birth)
        else: 
           Birth = 'Unknown'
         
         #  print(Birth)
        
        
        
        
        
        condition_7 = ppl.find('h3', text='Ethnicity: ')
        
        if condition_7 != None:
            
            Ethnicity = condition_7.next_sibling.next_sibling.get_text()
           
           # print(Ethnicity)
        else: 
           Ethnicity = 'Unknown'
          
          # print(Ethnicity)
        
        
        
        
        condition_8 = ppl.find('h3', text='Occupation: ')
        
        if condition_8 != None:
            
            Occupation = condition_8.next_sibling.next_sibling.get_text()
           
           # print(Occupation)
        else: 
           Occupation = 'Unknown'
          
          # print(Occupation)
        
        
        
        
        
        condition_9 = ppl.find('h3', text='Education: ')
        
        
        if condition_9 != None:
            
            Education = condition_9.next_sibling.next_sibling.get_text()
           
           # print(Education)
        else: 
           Education = 'Unknown'
           
           #print(Education)
        
        
        
        
        condition_10 = ppl.find('h3', text='Children: ')
        
        if condition_10 != None:
            
            Children = condition_10.next_sibling.next_sibling.get_text()
            
            #print(Children)
        else: 
           Children = 'Unknown'
            
            #print(Children)
        
        
        
        #print(ppl.find_all('h3'))
        dictio[Name] = [net_worth, source_of_wealth, Age, Place, Status, Nationality, Birth, Ethnicity, Occupation, Education, Children]
        
        #print(dictio)
        
        
        
        data = pd.DataFrame.from_dict(dictio)
        data_transposed = data.T
        print(data)

#print(data)
        
        data_transposed.to_excel('Billionaire.xlsx')