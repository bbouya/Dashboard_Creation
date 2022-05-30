import pandas as pd
import plotly.express as px
import streamlit as st

df = pd.read_excel(
    io = 'supermarkt_sales.xlsx',
    engine = 'openpyxl',
    sheet_name = 'Sales',
    usecols = 'B:R',
    nrows = 1000,
)
# Print some of data 
print(df.head())