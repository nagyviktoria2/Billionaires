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

'''
# Usage example
functional_pages = load_sites_to_visit()
print(functional_pages)
'''