import pandas as pd
import streamlit as st



Data=pd.read_csv('https://github.com/leone2497/Analysis/blob/main/owid-energy-data.csv')


st.title("Energy market - dashboard")
st.sidebar.title("type of analysis")
dictionary_type = st.sidebar.selectbox("Analysis", ["Dataset"])

