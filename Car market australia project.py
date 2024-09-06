import pandas as pd
import streamlit as st
import seaborn as sn
import matplotlib.pyplot as plt

cars_market_australia= pd.read_csv("/content/drive/MyDrive/Dati_lavoro/car market australia.csv")
cars_market_australia

st.title("Australia cars market analysis")
st.sidebar.title("Type of analysis")
type_analysis = st.sidebar.selectbox("Choose type", ["Price distribution", "Sales datas", "Features"])


if type_analysis == "Feature":
  Filters = st.sidebar("Select filter",["Price","Seating Capacity","Gearbox"])
  Choice = st.sidebar("Brand or model",["Brand","Model"])
  brand_sales = cars_market_australia.groupby(Choice)[Filters].sort_values(ascending=False)
  brand_sales=  brand_sales.apply(lambda x: f'{x:,.0f}')
  brand_sales
elif type_analysis == "Sales datas":
  plt.figure(figsize=(6, 10))
  data=cars_market_australia['Brand'].value_counts().sort_values(ascending=True).plot(kind='barh')
  plt.show()
  



elif type_analysis == "Price distribution":
  Filters = st.sidebar("Select filter",["histogram","lines"])
  if Filters =="histogram":
    sn.histplot(df, x=cars_market_australia['Price'], kde=True, log_scale=True)
    plt.show()
  elif Filters =="lines":
    sn.lineplot(x='Brand', y='Price', data=cars_market_australia)
    plt.show()


