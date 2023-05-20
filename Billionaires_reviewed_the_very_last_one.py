import requests
from bs4 import BeautifulSoup


sites_to_visit = []

base_url = "https://www.therichest.com/top-lists/top-250-richest-people-in-the-world/page/"
page_number = 1

# Loop until there are no more functional pages
while True:
    site = f"{base_url}{page_number}/"
    
    try:
        # Send a GET request and check the status code
        response = requests.get(site)
        response.raise_for_status()  # Raise an exception for non-200 status codes
        
        sites_to_visit.append(site)
        page_number += 1
    except requests.exceptions.RequestException:
        break

    print(sites_to_visit)
