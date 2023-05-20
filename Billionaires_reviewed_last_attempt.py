import requests
from bs4 import BeautifulSoup

N = 20
sites_to_visit = []
valid_sites = []  # List to store valid sites

base_url = "https://www.therichest.com/top-lists/top-250-richest-people-in-the-world/page/"

# Loop through all the pages and add them to the sites_to_visit list
for i in range(1, N + 1):
    site = f"{base_url}{i}/"
    sites_to_visit.append(site)

for site in sites_to_visit:
    response = requests.get(site)
    soup = BeautifulSoup(response.content, 'lxml')
    tags = soup.find_all('td', class_='rank')

    contains_valid_tag = False
    for tag in tags:
        if '250' in tag.get_text():
            contains_valid_tag = True
            break
#get the number of the site that contains the 250th person assign it to N and first then use the n in the loop
    if contains_valid_tag:
        valid_sites.append(site)

print(valid_sites)
