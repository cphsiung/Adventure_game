# Note only, not a functional code
import pandas as pd
from openpyxl.workbook import Workbook

df_excel = pd.read_excel('regions.xlsx')
df_csv = pd.read_csv('Names.csv', header=None)
df_txt = pd.read_csv('data.txt', delimiter='\t') # separated by text
# add header to csv file
df_csv.columns = ['First Name', 'Last Name', 'Address', 'City', 'State', 'Area Code']
# save csv file to Excel
df_csv.to_excel('modified.xlsx')

# return 2 columns (note the double bracket)
print(df_csv[['First Name','Last Name']])
# only shows First Name for first 3 records
print(df_csv['First Name'][0:3])

# save a certain search to Excel file
wanted_values = df[['First Name','Last Name','State']]
stored = wanted_values.to_excel('State_Location.xlsx', index=None)

#---------------------------
# Filters
#---------------------------
# Show only records with city equals Riverside
print(df_csv.loc(df_csv['City'] == 'Riverside'))
# Show records with city equals Riverside and First Name John
print((df_csv.loc[df_csv['City'] == 'Riverside') & (df_csv['First Name'] == 'John')])
