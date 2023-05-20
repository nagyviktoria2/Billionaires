import requests
from bs4 import BeautifulSoup

N=20
sites_to_visit = []
#def get_raw_richies(N: int, sites_to_visit):
base_url = "https://www.therichest.com/top-lists/top-250-richest-people-in-the-world/page/"
        #empty list to store all sites to visit

    # Loop through all the pages and add them to the sites_to_visit list
for i in range(1, N+1):
        site = f"{base_url}{i}/"
        sites_to_visit.append(site)

print(sites_to_visit)

#get_raw_richies(N=20, sites_to_visit)

personal_sites = []

for site in sites_to_visit:
    response = requests.get(site)
    soup = BeautifulSoup(response.content, 'lxml')

    
    tags = soup.find_all('td', class_='rank')



    for tag in tags:
        if '250' in tag.get_text():
            # Found the desired tag containing '250'
            break

    if '250' in tag.get_text():
        # Found the desired tag containing '250'
        break

    # Continue looping through the next URL
