from F_load_html_function import load_html_document
from F_get_hrefs_function import extract_href_with_prefix
from A_a_json_writer import write_to_json

loaded_html = load_html_document(file_name='combined_data.html')
hrefs = extract_href_with_prefix(loaded_html, tag='a', prefix='/celebnetworth/', class_name='')
#print(hrefs)
    
prefix = 'https://www.therichest.com'


def join_prefix_and_links(hrefs, prefix):
    """
    Joins a prefix with a list of links.

    Args:
        hrefs (list): A list of links to join with the prefix.
        prefix (str): The prefix to join with the links.

    Returns:
        list: A list of joined prefix and links.

    Example:
        hrefs = ['/link1', '/link2', '/link3']
        prefix = 'https://www.example.com'
        joined_links = join_prefix_and_links(hrefs, prefix)
        print(joined_links)
    """
    joined_links = [prefix + href for href in hrefs]

    return joined_links

joined_links_ppl = join_prefix_and_links(hrefs, prefix)

write_to_json('ppl_links.json', joined_links_ppl)

#print(joined_links_ppl)