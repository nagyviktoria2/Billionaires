'''
This code imports the function that loads the json file with functioning
sites (this json file is created in the file named: Get_list_functional sites),
and gets the number of the site that contains, in our case the 250. person. 
This number can be modified.
'''
import requests
from bs4 import BeautifulSoup
from B_load_json_file_fction import load_sites_to_visit

sites_to_visit = load_sites_to_visit('sites_to_visit.json')

def find_valid_sites(sites_to_visit, number):
    """
    Finds the first valid site from a list of URLs that contains the specified number in the tag.
    Prints the extracted number if a valid site is found.

    Arguments:
    - sites_to_visit (list): A list of URLs to visit.
    - number (str or int): The number to search for in the tag.

    Returns:
    - extracted_number (str): The extracted number from the valid site's URL, or None if no valid site is found.
    """
    extracted_number = None

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
            extracted_number = site.split('/')[-2]
            #print(extracted_number)
            break

    if extracted_number is None:
        print("No valid site found.")

    return extracted_number

# Example usage:
'''
number_to_search = 250

extracted_number = find_valid_sites(sites_to_visit, number_to_search)

print(extracted_number)

N = extracted_number
'''