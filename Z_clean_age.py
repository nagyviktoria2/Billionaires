import pandas as pd

df = pd.read_excel('Bili.xlsx')

#print(data['age'])

df['age'] = df['age'].replace('Unknown', pd.NA)

df['age'] = pd.to_numeric(df['age'])

average_age = df['age'].mean()

df['age'] = df['age'].fillna(average_age)

#print(average_age)


print(df['age'])
