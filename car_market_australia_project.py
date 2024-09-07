#pip install seaborn matplotlib pandas streamlit
import pandas as pd
import streamlit as st
import seaborn as sn
import matplotlib.pyplot as plt

# Load dataset
cars_market_australia = pd.read_csv("https://raw.githubusercontent.com/leone2497/Analysis/main/car%20market%20australia.csv")
st.title("Australia Cars Market Analysis")

# Sidebar selection
st.sidebar.title("Type of analysis")
type_analysis = st.sidebar.selectbox("Choose type", ["Price distribution", "Sales datas", "Features"])

if type_analysis == "Features":
    Filters = st.sidebar.selectbox("Select filter", ["Price", "Seating Capacity"])
    Choice = st.sidebar.selectbox("Brand or model", ["Brand", "Model"])
    
    # Group by selected filter and choice
    brand= cars_market_australia[[Choice, Filters]].sort_values(by= Filters, ascending=True)
    
    
    # Display the results
    st.write(brand)

elif type_analysis == "Sales datas":
    # Plot a horizontal bar plot
    plt.figure(figsize=(6, 10))
    data = cars_market_australia['Brand'].value_counts().sort_values(ascending=True).plot(kind='barh')
    
    # Display the plot in Streamlit
    st.pyplot(plt)
    plt.clf()

elif type_analysis == "Price distribution":
    # Choose type of plot
    Filters = st.sidebar.selectbox("Select filter", ["histogram", "lines"])
    
    if Filters == "histogram":
        # Plot a histogram of car prices
        sn.histplot(cars_market_australia, x='Price', kde=True, log_scale=True)
        st.pyplot(plt)
        plt.clf()
        
    elif Filters == "lines":
        # Plot a line plot of prices per brand
        sn.lineplot(x='Brand', y='Price', data=cars_market_australia)
        st.pyplot(plt)
        plt.clf()
