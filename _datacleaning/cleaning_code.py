# %%
#Setting up workplace
import json
import pandas as pd
import numpy as np
import re
from dateutil import parser

# %%
with open('people_info.json', 'r') as file: #load it from your library, later it will be on github so it can be loaded from there 
    data = json.load(file)
df = pd.DataFrame(data.values(), index=data.keys(), columns=[
    "Net Worth", "Industry", "Age", "Birthplace", "Marital Status",
    "Nationality", "Date of Birth", "Citizenship", "Occupation", "Education", "Children"
])

# %%
#resetting index, naming first column 
df = df.rename(columns={'Unnamed: 0': 'Name'})
df.reset_index(inplace=True)
df.index.name = "Index"
df = df.rename(columns = {"index" : "Name"})

# %%
#Dropping Citizenship column 
df = df.drop('Citizenship', axis=1)

# %%
#cleaning the column "Name"
#deleting unknown values 
df = df[df["Name"] != "Unknown"]

# %%
#Replacing "Unknown" to missing values 
df = df.replace("Unknown", np.nan)

# %%
#cleaning "Age" column
 
def replace_missing_with_mean(df, column):
    """
    Replace missing values in a column of a dataframe with the mean value of the column and change the datatype of the column.
    
    Args:
        df (DataFrame): The dataframe containing the column.
        column (str): The name of the column in the dataframe.
        
    Returns:
        DataFrame: The modified dataframe with missing values replaced by mean value and datatype changed.
    """
    # Create a separate dataframe with the specified column and drop missing values
    column_df = pd.DataFrame({column: df[column]})
    column_df = column_df.dropna()
    
    # Calculate the mean value of the column
    column_df[column] = column_df[column].astype(int)
    mean_value = column_df[column].mean()
    
    # Replace missing values in the column with the mean value
    df[column] = df[column].fillna(mean_value)
    
    # Change the datatype of the column to match the original values
    df[column] = df[column].astype(column_df[column].dtype)
    
    return df

df = replace_missing_with_mean(df, 'Age')

# %%
#Cleaning "Net Worth"
#removing characters 
df["Net Worth"] = df["Net Worth"].str.replace("$", "")
df["Net Worth"] = df["Net Worth"].str.replace("Billion", "")
#changing datatype 
df["Net Worth"] = df["Net Worth"].astype(float)

# %%
#cleaning birthplace column 
#created a copy column 
birthcountry = df['Birthplace'].str.split(', ').str[-1]
birthcountry

#manually cleaning some outlier values 
birthcountry = birthcountry.str.replace(")", "")
birthcountry = birthcountry.str.replace("Prague", "Czech Republic")

def replace_values_in_column(column, replace_list, replace_with):
    """
    Replace specified values in a column with a given country.
    
    Args:
        column (Series): The column to perform replacements on.
        replace_list (list): The list of values to be replaced.
        replace_with (str): The country to replace the values with.
        
    Returns:
        Series: A new column with the replaced values.
    """
    # Replace specified values in the column with the given country
    column = column.str.replace('|'.join(replace_list), replace_with)

    # Drop everything else besides the replace value
    column = column.str.replace('(.*' + replace_with + ').*', r'\1')
    
    # Remove duplicate consecutive words in each value
    column = column.str.replace(r'\b(\w+)\b\s+\1', r'\1')
    
    return column
#cleaning the United States, creating a list of the states and possible othen names
statesplus = ["U.S.", "United States of America", "USA", "Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming" ]
birthcountry = replace_values_in_column(birthcountry, statesplus, "United States")

#cleaning China, creating list of provinces and other names, dropping other values 
chinaplus = ["PRC", "Republic of China", "Anhui", "Fujian", "Gansu", "Guangdong", "Guizhou", "Hainan", "Hebei", "Heilongjiang", "Henan", "Hubei", "Hunan", "Jiangsu", "Jiangxi", "Jilin", "Liaoning", "Qinghai", "Shaanxi", "Shandong", "Shanxi", "Sichuan", "Yunnan", "Zhejiang", "Guangxi", "Nei Mongol", "Ningxia", "Xinjiang", "Xizang", "Beijing", "Chongqing", "Shanghai", "Tianjin", "Hong Kong", "Macau"]
birthcountry = replace_values_in_column(birthcountry, chinaplus, "China")

# dropping everything else besides country name 
birthcountry = birthcountry.str.replace(r'^.*?(\bAustralia\b).*$', r'\1')
birthcountry = birthcountry.str.replace(r'^.*?(\bIndonesia\b).*$', r'\1')

# deleting numbers then replacing empty values to missing 
birthcountry = birthcountry.str.replace(r'\d+', '')
birthcountry = birthcountry.replace('', np.nan)

#Adding it back to the original dataframe 
df['Birthplace'] = birthcountry

# %%
#cleaning Marital Status, removing the names in the brakets
df['Marital Status'] = df['Marital Status'].str.replace(r"\(.*\)", "", regex=True)

# %%
#cleaning Nationality
df['Nationality'] = df['Nationality'].str.replace(r'[-&]| and ', ', ', regex=True) #creating consistent format

#dictionary of some countries to fix 
nationalities = {
    'United States': 'American',
    'China': 'Chinese',
    'France': 'French',
    'Germany': 'German',
    'Italy': 'Italian',
    'Spain': 'Spanish',
    'Canada': 'Canadian',
    'Australia': 'Australian',
    'Brazil': 'Brazilian',
    'India': 'Indian',
    'Mexico': 'Mexican',
    'Sweden': 'Swedish',
    'Russia': 'Russian',
    'United Kingdom': 'British',
    'England': 'Enlgish',
    'Switzerland': 'Swiss',
    'Saudi Arabia': 'Saudi Arabian',
    'Colombia': 'Colombian',
    'Finland': 'Finnish',
    'Nigeria': 'Nigerian',
}

#Function to fix the data
def fix_nationalities(df, column_name, mapping_dict):
    """
    Fix inconsistent nationalities in a column using string replace with a mapping dictionary.
    
    Args:
        df (DataFrame): The DataFrame containing the column to be fixed.
        column_name (str): The name of the column to be fixed.
        mapping_dict (dict): A mapping dictionary with inconsistent values as keys and their corresponding replacements as values.
        
    Returns:
        DataFrame: The modified DataFrame with fixed column values.
    """
    df = df.copy()  # Create a copy of the DataFrame
    
    try:
        for key, value in mapping_dict.items():
            df[column_name] = df[column_name].str.replace(key, value)
        
        df[column_name] = df[column_name].str.replace(r'nn$', 'n', regex=True) #removing double endings 
    except Exception as e:
        print(f"An error occurred: {e}")
    
    return df

df = fix_nationalities(df, 'Nationality', nationalities)

# %%
#Cleaning Date of birth 
df['Date of Birth'] = df['Date of Birth'].astype(str)
Date_col = pd.DataFrame({"Date of Birth": df["Date of Birth"]})
Date_col

def convert_year_only_to_missing(df, column_name):
    """
    Convert year-only values in a column to missing values.
    
    Args:
        df (DataFrame): The DataFrame containing the column.
        column_name (str): The name of the column.
        
    Returns:
        DataFrame: The modified DataFrame with year-only values converted to missing values.
    """
    df = df.copy()  # Create a copy of the DataFrame
    
    try:
        # Define a regular expression pattern to match year-only values
        pattern = r'^\d{4}$'
        
        # Use regular expressions and string manipulation to convert year-only values to missing values
        df[column_name] = df[column_name].apply(lambda x: np.nan if pd.isnull(x) else x if re.match(pattern, str(x)) is None else np.nan)
    except Exception as e:
        print(f"An error occurred: {e}")
    
    return df

Date_col = convert_year_only_to_missing(Date_col, 'Date of Birth')

def convert_to_date_month_year(df, column_name):
    """
    Convert dates in different formats to 'date month year' format.
    
    Args:
        df (DataFrame): The DataFrame containing the date column.
        column_name (str): The name of the date column.
        
    Returns:
        DataFrame: The modified DataFrame with dates converted to 'date month year' format.
    """
    df = df.copy()  # Create a copy of the DataFrame
    
    try:
        df[column_name] = pd.to_datetime(df[column_name], errors='coerce')
        df[column_name] = df[column_name].dt.strftime("%d %B %Y")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    return df

Date_col = convert_to_date_month_year(Date_col, 'Date of Birth')

df['Date of Birth'] = Date_col['Date of Birth']

# %%
#Creating a column for Zodiac signs
def get_zodiac_sign(date):
    if pd.isnull(date):
        return np.nan
    
    try:
        day, month, year = date.split(' ')
        month = pd.to_datetime(month, format='%B').month
        day = int(day)
    
        if (month == 1 and day >= 20) or (month == 2 and day <= 18):
            return 'Aquarius'
        elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
            return 'Pisces'
        elif (month == 3 and day >= 21) or (month == 4 and day <= 19):
            return 'Aries'
        elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
            return 'Taurus'
        elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
            return 'Gemini'
        elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
            return 'Cancer'
        elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
            return 'Leo'
        elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
            return 'Virgo'
        elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
            return 'Libra'
        elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
            return 'Scorpio'
        elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
            return 'Sagittarius'
        else:
            return 'Capricorn'
    except ValueError:
        return np.nan
    
df['Zodiac Sign'] = df['Date of Birth'].apply(get_zodiac_sign)

# %%
#cleaning Children column 

#creating a new column by dropping the information in brackets after the numbers
filtered_data = df['Children'].str.replace(r'\(.*\)', '', regex=True)
filtered_data.astype(str)

#replacing 'and'-s with commas, so values are countable 
filtered_data = filtered_data.str.replace(' and ', ', ', regex=False)

###
def replace_with_counts(column):
    """
    Replace the values separated by commas with their respective counts,
    while leaving the values with only one word or a number unchanged.
    
    Args:
        column (Series): The column to replace the values in.
        
    Returns:
        Series: A new column with the modified values.
    """
    def replace(row):
        # Check if the value contains commas
        if ',' in str(row):
            # Split the value by commas and count the number of items
            items = str(row).split(',')
            count = len(items)
            
            # Return the count as a string
            return str(count)
        
        # Return the original value for single words or numbers
        return str(row)
    
    return column.apply(replace)

filtered_data = replace_with_counts(filtered_data)

###
def convert_and_drop(column):
    """
    Convert written numbers to actual numbers and drop everything after the first number or word in each value of a column.
    
    Args:
        column (Series): The column to convert and modify.
        
    Returns:
        Series: A new column with the modified values.
    """
    def convert(row):
        # Define a mapping of written numbers to actual numbers
        number_mapping = {
            'None': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
            'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10,
            'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14, 'fifteen': 15
        }
        
        # Extract the first number or word from the value
        for word in str(row).split():
            if word in number_mapping:
                # Convert written numbers to actual numbers
                return number_mapping[word]
            elif word.isdigit():
                # Return the first number encountered
                return int(word)
        
        # Return None if no number or word is found
        return None
    
    return column.apply(convert)

filtered_data = convert_and_drop(filtered_data)

#Placing it back to the original dataframe 
df['Children'] = filtered_data


