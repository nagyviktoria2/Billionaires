import json

# Read the JSON file and load the list
with open('sites_to_visit.json', 'r') as file:
    sites_to_visit = json.load(file)

# Access the sites_to_visit list
print(sites_to_visit)
