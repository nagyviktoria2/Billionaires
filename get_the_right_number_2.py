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
    Finds the first valid site from a list of URLs that contains the specified number in the tag.

    Arguments:
    - sites_to_visit (list): A list of URLs to visit.
    - number (str or int): The number to search for in the tag.

    Returns:
    - valid_site (str): The URL of the first site that contains the specified number in the tag, or None if no site is found.
    """
    valid_site = None

    for site in sites_to_visit:
        response = requests.get(site)
        soup = BeautifulSoup(response.content, 'lxml')
        tags = soup.find_all('td', class_='rank')

        contains_valid_tag = False
        for tag in tags:
            if tag.get_text().strip() == str(number):  # Check for exact match with the number
                contains_valid_tag = True
                break

        if contains_valid_tag:
            valid_site = site
            break

    return valid_site

# Example usage:

number_to_search = 250

valid_site = find_valid_sites(sites_to_visit, number_to_search)

if valid_site:
    extracted_number = valid_site.split('/')[-2]
    print(extracted_number)
else:
    print("No valid site found.")
