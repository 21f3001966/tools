# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "pandas",
#  
# ]
# ///



import pandas as pd

df = pd.read_csv('data.csv')

print(df.info)