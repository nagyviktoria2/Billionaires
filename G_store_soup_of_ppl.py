from B_load_json_file_fction import load_sites_to_visit
from E_Get_and_save_html_of_base_sites import persist_html_content

ppl_urls = load_sites_to_visit('ppl_links.json')

persist_html_content(ppl_urls, 'ppl_soup.html')

