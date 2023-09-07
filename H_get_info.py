from F_load_html_function import load_html_document
from A_a_json_writer import write_to_json


def get_value(ppl, text):
    """
    Retrieves the value associated with a specific text label from a BeautifulSoup object.

    Parameters:
        ppl (BeautifulSoup object): The BeautifulSoup object containing the HTML content.
        text (str): The text label to search for in the BeautifulSoup object.

    Returns:
        str: If the text label is found, returns the corresponding value as a string.
             If the text label is not found, returns 'Unknown' as a string.
    """
    condition = ppl.find('h3', text=text)
    if condition is not None:
        return condition.next_sibling.next_sibling.get_text()
    else:
        return 'Unknown'

def get_person_info(ppl):
    """
    Extracts information about a person from a BeautifulSoup object.

    Parameters:
        ppl (BeautifulSoup object): The BeautifulSoup object containing the HTML content of a person's data.

    Returns:
        tuple: A tuple containing the person's full name as a string and a list of their information.
        The list contains the following information (in order):
            - Net worth
            - Source of wealth
            - Age
            - Birth place
            - Marital status
            - Nationality
            - Date of birth
            - Ethnicity
            - Occupation
            - Education
            - Children
    """
    net_worth = ppl.find('strong', class_='net-profile_header_networth').get_text() if ppl.find('strong', class_='net-profile_header_networth') else 'Unknown'
    source_of_wealth = get_value(ppl, 'Source of Wealth: ')
    age = get_value(ppl, 'Age: ')
    birth_place = get_value(ppl, 'Birth Place: ')
    marital_status = get_value(ppl, 'Marital Status: ')
    full_name = get_value(ppl, 'Full Name: ')
    nationality = get_value(ppl, 'Nationality: ')
    date_of_birth = get_value(ppl, 'Date of Birth: ')
    ethnicity = get_value(ppl, 'Ethnicity: ')
    occupation = get_value(ppl, 'Occupation: ')
    education = get_value(ppl, 'Education: ')
    children = get_value(ppl, 'Children: ')

    return full_name, [net_worth, source_of_wealth, age, birth_place, marital_status, nationality, date_of_birth, ethnicity, occupation, education, children]




def create_dictio_from_html(ppl):
    """
    Creates a dictionary of person information from a BeautifulSoup object.

    Parameters:
        ppl (BeautifulSoup object): The BeautifulSoup object containing the HTML content.

    Returns:
        dict: A dictionary where the keys are the person's full names and the values are lists of their information.
    """
    dictio = {}
    for person_data in ppl.find_all('div', class_='w-content'):
        name, info = get_person_info(person_data)
        dictio[name] = info
    return dictio

# Usage example
'''
ppl = load_html_document(file_name='ppl_soup.html', parser='html.parser')
dictio = create_dictio_from_html(ppl)
print(dictio)

write_to_json('people_info.json', dictio)
'''