# Read from URL data and store it to csv : 

# import library : 
import pandas as pd
import requests as re
import urllib.request as req
import io
url = 'https://raw.githubusercontent.com/Lexie88rus/bank-marketing-analysis/master/bank.csv'
 
data = re.get(url).content

# We are getting a HTML back not a csv file so it is not going to work

data = pd.read_csv(io.StringIO(data.decode('utf-8')))

print(data.head())

data.to_csv('bank.csv')