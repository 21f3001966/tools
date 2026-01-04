# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "chardet",
#    "pandas"
# ]
# ///




import chardet
with open('dummy.txt','rb') as f:
    result = chardet.detect(f.read()) 
print(result['encoding'])


with open('dummy.txt',encoding=result['encoding']) as f:
    text = f.read()
    #print(text)


import pandas as pd

df = pd.read_csv('data.csv',encoding='ascii')
print(df.head())