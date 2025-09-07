"""
This file reads an HTML file containing a table of data and converts it into a cleaned CSV format.

"""


import pandas as pd

tables = pd.read_html('table_data.html')
df = tables[0]
df.to_csv('cleaned_data.csv', index=False)