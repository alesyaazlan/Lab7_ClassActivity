import streamlit as st
import pandas as pd
import numpy as np
import folium
from streamlit_folium import st_folium
import geopandas as gpd
from folium.plugins import HeatMap
import plotly.express as px

# Streamlit page setup
st.set_page_config(
    page_title="Global COVID-19 Heatmap",
    page_icon="🦠",
    layout="wide"
)

# --- Load Data Function ---
@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/datasets/covid-19/main/data/countries-aggregated.csv"
    df = pd.read_csv(url)
    df['Date'] = pd.to_datetime(df['Date'])   # ✅ Corrected: pd.to_datetime
    return df

# Load dataset
df = load_data()

# --- Sidebar filters ---
st.sidebar.header("Filter Options")
country = st.sidebar.selectbox("Select Country", df['Country'].unique())
metric = st.sidebar.radio("Select Metric", ['Confirmed', 'Recovered', 'Deaths'])  # ✅ Added missing comma between 'Confirmed' and 'Recovered'

# --- Filtered data ---
filtered_df = df[df['Country'] == country]

# --- Line chart ---
fig = px.line(filtered_df, x='Date', y=metric, title=f"{metric} Cases in {country}")
st.plotly_chart(fig, use_container_width=True)

# --- Optional raw data ---
if st.checkbox("Show Raw Data"):
    st.write(filtered_df)

# --- Additional section ---
st.markdown("---")
st.subheader("Additional Visualization")
st.write("Here you could add a global map, a heatmap, or comparison between countries using the same dataset.")
