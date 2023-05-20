
'''
from load_json_file_fction import load_sites_to_visit
from Get_sites_up_to_x_site_list import get_urls_up_to_number

number = 250 #still, one can change the number. such action retrieves different # of sites
sites_to_visit = load_sites_to_visit()
urls = get_urls_up_to_number(sites_to_visit, number)

for url in urls:
    ##send get request to urls and store the response:
    response = requests.get(url)
    
    ##create a beautifulsoup object from the content of the response:
    soup = BeautifulSoup(response.content, 'lxml')

    #persist the data as html: 
    with open('data.html', 'w') as file:
    file.write(str(soup))
'''

import requests
from bs4 import BeautifulSoup
from load_json_file_fction import load_sites_to_visit
from Get_sites_up_to_x_site_list import get_urls_up_to_number

def persist_html_content(number, file_name='combined_data.html'):
    """
    Fetches the HTML content of web pages and persists it as a single HTML document.

    Args:
        number (int): The number of web pages to fetch and combine.
        file_name (str): The name of the output HTML file. Default is 'combined_data.html'.

    Returns:
        None
    """
    # Load the list of sites to visit
    sites_to_visit = load_sites_to_visit()

    # Get the URLs up to the specified number
    urls = get_urls_up_to_number(sites_to_visit, number)

    # Create an empty string to store the combined HTML content
    combined_html = ""

    for url in urls:
        # Send GET request to the URL and store the response
        response = requests.get(url)

        # Create a BeautifulSoup object from the content of the response
        soup = BeautifulSoup(response.content, 'lxml')

        # Append the HTML content to the combined HTML string
        combined_html += str(soup)

    # Persist the combined HTML content as a single HTML file
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(combined_html)

    print(f"HTML content persisted to {file_name}.")

# Example usage
persist_html_content(number=250, file_name='combined_data.html')

