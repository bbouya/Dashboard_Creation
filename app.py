from distutils.fancy_getopt import OptionDummy
from enum import unique
import pandas as pd
import plotly.express as px
from sklearn.metrics import average_precision_score
import streamlit as st

# Emoji from a webite 'https://www.webfx.com/tools/emoji-cheat-sheet'

st.set_page_config(page_title = 'Sales Dashboard',
                page_icon = ':bar_chart:',
                layout = 'wide'
                )

df = pd.read_excel(
    io = 'supermarkt_sales.xlsx',
    engine = 'openpyxl',
    sheet_name = 'Sales',
    usecols = 'B:R',
    nrows = 1000,
    header = 3,
)

# Print some of data
print(df.head())
test = df.astype(str)

st.dataframe(test)

# ----- SIDEBAR ---- 
st.sidebar.header('Please filter Here:')
city = st.sidebar.multiselect(
        'Select the City:',
        options = df['City'].unique(),
        default = df['City'].unique()
)

customer_type = st.sidebar.multiselect(
    'Select The Customer Type',
    options = df['Customer_type'].unique(),
    default = df['Customer_type'].unique()
)

gender = st.sidebar.multiselect(
    'Select the Gender',
    options = df['Gender'].unique(),
    default = df['Gender'].unique()
)

df_selection = df.query(
    'City == @city & Customer_type == @customer_type & Gender == @gender'
)

# --- MainPage ---
st.title(":bar_chart: Sales Dashboard")
st.markdown("##")

# Top KPI's
total_sales = int(df_selection['Total'].sum())
average_rating = round(df_selection['Rating'].mean(),2)
star_rating = ":star:" * int(round(average_rating, 0))
average_sales_by_transaction = round(df_selection['Total'].mean(),2)

