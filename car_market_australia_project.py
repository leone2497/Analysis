import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

cars_market_australia = pd.read_csv("https://raw.githubusercontent.com/leone2497/Analysis/main/car%20market%20australia.csv")
st.title("Australia Cars Market Analysis")

st.sidebar.title("Type of analysis")
type_analysis = st.sidebar.selectbox("Choose type", ["Price distribution", "Sales datas", "Features"])

if type_analysis == "Features":
    Filters = st.sidebar.selectbox("Select filter", ["Price", "Seating Capacity"])
    Choice = st.sidebar.selectbox("Brand or model", ["Brand", "Model"])
    
    brand = cars_market_australia[[Choice, Filters]].sort_values(by=Filters, ascending=True)
    st.write(brand)

elif type_analysis == "Sales datas":
    plt.figure(figsize=(6, 10))
    data = cars_market_australia['Brand'].value_counts().sort_values(ascending=True).plot(kind='barh')
    st.pyplot(plt)
    plt.close()

elif type_analysis == "Price distribution":
    Filters = st.sidebar.selectbox("Select filter", ["histogram", "lines"])
    
    if Filters == "histogram":
        sns.histplot(cars_market_australia, x='Price', kde=True, log_scale=True)
        st.pyplot(plt)
        plt.close()
        
    elif Filters == "lines":
        sns.lineplot(x='Brand', y='Price', data=cars_market_australia)
        st.pyplot(plt)
        plt.close()
