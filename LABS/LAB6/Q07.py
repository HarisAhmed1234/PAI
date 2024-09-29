import pandas as pd

df = pd.read_excel('employee.xlsx', engine='openpyxl')

specified_year = 2021
employees_in_year = df[df['Year'] == specified_year]
print(employees_in_year)
