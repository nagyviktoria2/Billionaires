import requests
import json
from A_a_json_writer import write_to_json

def visit_functional_pages(base_url):
    """
    Visit functional pages until a non-functional page is encountered or an exception occurs.

    Args:
        base_url (str): The base URL of the pages to visit.

    Returns:
        list: A list of functional page URLs visited.

    Raises:
        requests.exceptions.RequestException: If an error occurs during the GET request.

    """
    global sites_to_visit   # Making the list a global variable to be able to access it later/by other functions
    sites_to_visit = []
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
        except requests.exceptions.RequestException as e:
            # Handle request exceptions (e.g., connection error, timeout)
            print(f"An error occurred while accessing {site}: {e}")
            break


    return sites_to_visit

base_url = "https://www.therichest.com/top-lists/top-250-richest-people-in-the-world/page/"
functional_pages = visit_functional_pages(base_url)
print(functional_pages)

# Save the list to a JSON file using the write_to_json function
write_to_json('sites_to_visit.json', functional_pages)