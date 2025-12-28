import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

st.set_page_config(page_title="Voltage Data Dashboard", layout="wide")
st.title("Voltage Data Analysis Dashboard")

@st.cache_data
def load_data():
    data = {}
    try: data['main'] = pd.read_csv('Sample_Data.csv').rename(columns={'Values':'Voltage'})
    except: data['main'] = pd.DataFrame()
    try: data['peaks'] = pd.read_csv('voltage_peaks.csv')
    except: data['peaks'] = pd.DataFrame()
    try: data['lows'] = pd.read_csv('voltage_lows.csv')
    except: data['lows'] = pd.DataFrame()
    try: data['below_20'] = pd.read_csv('voltage_below_20.csv')
    except: data['below_20'] = pd.DataFrame()
    try: data['downward'] = pd.read_csv('voltage_downward_acc.csv')
    except: data['downward'] = pd.DataFrame()
    return data

data = load_data()

tabs = st.tabs(["Overview", "Main Data", "Peaks & Lows", "Special Conditions", "Visualizations"])
with tabs[0]:
    st.subheader("Dataset Overview")
    for name, df in data.items():
        if not df.empty:
            st.write(f"**{name.upper()}**: {len(df)} records")
        else:
            st.write(f"**{name.upper()}**: No data available")

with tabs[1]:
    st.subheader("Main Voltage Data")
    if not data['main'].empty:
        st.dataframe(data['main'])
    try:
        img = Image.open('voltage_plot.png')
        st.image(img, caption="Voltage Over Time")
    except: st.write("Image file not found")

with tabs[2]:
    st.subheader("Peaks and Lows")
    col1, col2 = st.columns(2)
    with col1:
        st.write("**Peaks**")
        if not data['peaks'].empty: st.dataframe(data['peaks'])
    with col2:
        st.write("**Lows**")
        if not data['lows'].empty: st.dataframe(data['lows'])

with tabs[3]:
    st.subheader("Special Conditions")
    col1, col2 = st.columns(2)
    with col1:
        st.write("**Below 20V**")
        if not data['below_20'].empty: st.dataframe(data['below_20'])
    with col2:
        st.write("**Downward Acceleration**")
        if not data['downward'].empty: st.dataframe(data['downward'])

with tabs[4]:
    st.subheader("Visualizations")
    try:
        img = Image.open('voltage_ma.png')
        st.image(img, caption="Voltage Moving Average")
    except: st.write("Image file not found")