from B_load_json_file_fction import load_sites_to_visit

list = load_sites_to_visit('ppl_links.json')

print(len(list))


import requests

def check_urls(urls):
    results = {}
    
    for url in urls:
        try:
            response = requests.head(url)
            results[url] = response.status_code == requests.codes.ok
        except requests.ConnectionError:
            results[url] = False
    
    return results



results = check_urls(list)
lst_working = []
lst_not_working = []
for url, is_working in results.items():
    if is_working:
        (f"{url} is working")
        lst_working.append(url)
    else:
        #print(f"{url} is not working")
        lst_not_working.append(url)

print(lst_not_working)
print(lst_working)
#fction returning fctional sites