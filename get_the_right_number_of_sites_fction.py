import requests
from bs4 import BeautifulSoup

import json

def load_sites_to_visit():
    """
    Load the list of functional page URLs from a JSON file.

    Returns:
        list: A list of functional page URLs.

    """
    with open('sites_to_visit.json', 'r') as file:
        sites_to_visit = json.load(file)

    return sites_to_visit

sites_to_visit = load_sites_to_visit()

def find_valid_sites(sites_to_visit, number):
    """
    Finds valid sites from a list of URLs by checking if they contain a specified number in a specific tag.

    Arguments:
    - sites_to_visit (list): A list of URLs to visit.
    - number (str or int): The number to search for in the tag.

    Returns:
    - valid_sites (list): A list of URLs that contain the specified number in the tag.
    """
    valid_sites = []

    for site in sites_to_visit:
        response = requests.get(site)
        soup = BeautifulSoup(response.content, 'lxml')
        tags = soup.find_all('td', class_='rank')

        contains_valid_tag = False
        for tag in tags:
            if str(number) in tag.get_text():
                contains_valid_tag = True
                break

        if contains_valid_tag:
            valid_sites.append(site)

    return valid_sites

# Example usage:

number_to_search = 250

valid_sites = find_valid_sites(sites_to_visit, number_to_search)
print(valid_sites)
