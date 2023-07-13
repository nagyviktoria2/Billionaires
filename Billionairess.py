

#Setting up workplace
import json
import pandas as pd
import numpy as np
     

with open('people_info.json', 'r') as file: #load it from your library, later it will be on github so it can be loaded from there 
    data = json.load(file)
df = pd.DataFrame(data.values(), index=data.keys(), columns=[
    "Net Worth", "Industry", "Age", "Birthplace", "Marital Status",
    "Nationality", "Date of Birth", "Citizenship", "Occupation", "Education", "Children"
])
     

#resetting index, naming first column 
df = df.rename(columns={'Unnamed: 0': 'Name'})
df.reset_index(inplace=True)
df.index.name = "Index"
df = df.rename(columns = {"index" : "Name"})
     

#cleaning the column "Name"
#deleting unknown values 
df = df[df["Name"] != "Unknown"]
     

#Replacing "Unknown" to missing values 
df = df.replace("Unknown", np.nan)
     

#cleaning "Age" column

#creating a separate "Age" dataframe and calculating the mean age
Age_column = pd.DataFrame({"Age": df["Age"]})
Age_column = Age_column.dropna()
Age_column["Age"] = Age_column["Age"].astype(int)
mean_age = Age_column["Age"].mean()

#replacing missing values by mean age
mean_age = int(mean_age)
df["Age"] = df["Age"].fillna(mean_age)


from B_fctn_drop_columns import drop_columns

df = drop_columns(df, columns = [
    "Net Worth", "Industry", "Birthplace", "Marital Status",
    "Nationality", "Date of Birth", "Citizenship", "Occupation", "Education", "Children"
])
#print(df)


import pandas as pd
import numpy as np

def find_billionaire_by_age(dataframe, age):
    """
    Finds the billionaire's name and age based on the input age or the closest age match.

    Args:
        dataframe (pd.DataFrame): DataFrame containing the billionaires' names and ages.
        age (int): The age to search for or find the closest match.

    Returns:
        str: The billionaire's name and age matching the input age or the closest age match.
    """
    # Convert the 'Age' column to integers
    dataframe['Age'] = dataframe['Age'].astype(int)

    # Calculate the absolute difference between each age in the DataFrame and the input age
    dataframe['Age_Difference'] = np.abs(dataframe['Age'] - age)

    # Sort the DataFrame by the age difference in ascending order
    sorted_df = dataframe.sort_values('Age_Difference')

    # Get the billionaire's name and age with the closest age match
    closest_billionaire = sorted_df.iloc[0]
    billionaire_name = closest_billionaire['Name']
    billionaire_age = closest_billionaire['Age']

    return f"{billionaire_name}, Age: {billionaire_age}"

'''
# Example usage
data = {
    'Name': ["Vladimir Vladimirovich Putin", "Jeffrey Preston 'Jeff' Bezos", "Elon Musk",
             "William Henry Gates III", "Bernard Jean Étienne Arnault", "Sandra Ortega Mera",
             "Jorn Rausing", "Pham Nhat Vuong", "Charles Gerald John Cadogan", "Paolo Rocca"],
    'Age': [68, 57, 49, 65, 72, 68, 61, 52, 84, 68]
}
df = pd.DataFrame(data)
'''




age = int(input("Enter the age: "))
billionaire_info = find_billionaire_by_age(df, age)
print(billionaire_info)








'''
df["Age"] = pd.to_numeric(df["Age"], errors='coerce')  # Convert "Age" column to numeric
sorted_df = df.sort_values("Age")
print(sorted_df["Age"])

'''

