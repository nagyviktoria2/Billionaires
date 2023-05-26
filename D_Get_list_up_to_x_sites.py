from C_Get_the_right_number_of_site import find_valid_sites
from B_load_json_file_fction import load_sites_to_visit

def get_urls_up_to_number(sites_to_visit, number_to_search):
    """
    Retrieves the URLs up to the specified number from a list of sites to visit.

    Arguments:
    - sites_to_visit (list): A list of URLs to visit.
    - number_to_search (int): The number to search for in the tag.

    Returns:
    - urls (list): A list of URLs up to the specified number, or an empty list if no valid site is found.
    """
    extracted_number = find_valid_sites(sites_to_visit, number_to_search)

    if extracted_number is not None:
        extracted_number = int(extracted_number)
        urls = sites_to_visit[:extracted_number]
        
    else:
        urls = []

    return urls


# Example usage:
'''
sites_to_visit = load_sites_to_visit('sites_to_visit.json')
number_to_search = 250
urls = get_urls_up_to_number(sites_to_visit, number_to_search)
print(urls)
'''
