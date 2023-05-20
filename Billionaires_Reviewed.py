import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_raw_richies(N: int):
    base_url = "https://www.therichest.com/top-lists/top-250-richest-people-in-the-world/page/"
    sites_to_visit = []    #empty list to store all sites to visit

    # Loop through all the pages and add them to the sites_to_visit list
    for i in range(1, N+1):
        site = f"{base_url}{i}/"
        sites_to_visit.append(site)

    print(sites_to_visit)

    # Scraping loop
    while sites_to_visit:
        site = sites_to_visit.pop(0)  # Get the first site to visit
        try:
            response = requests.get(site)
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                # Perform scraping operations here
                # ...
                # ...

                # Example: Print the page title
                #print(soup.title.text)

                #print(soup)

                # Example: Save data to a dataframe
                # df = pd.DataFrame(data)

                # Example: Append additional sites to visit
                # sites_to_visit.append(new_site)

        except requests.exceptions.RequestException as e:
            print(f"Error accessing site: {site}")
            print(e)

# Call the function to start scraping with N = 11
get_raw_richies(N=11)



    for site in sites_to_visit:
        response = requests.get(site)
        soup = BeautifulSoup(response, 'lxml')

        while site.body.find('td', class_= 'rank').get_text() != '250':