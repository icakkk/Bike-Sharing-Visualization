import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.header('Bike Sharing Dashboard :sparkles:')

# Load data
all_data = pd.read_csv('https://raw.githubusercontent.com/icakkk/Bike-Sharing-Visualization/main/dashboard/all_data.csv')
prediction_data = pd.read_csv('https://raw.githubusercontent.com/icakkk/Bike-Sharing-Visualization/main/dashboard/prediction_data.csv')

# Combine both datasets
combined_data = pd.concat([all_data, prediction_data])

# Function to filter data based on user selection
def filter_data(data, rental_type):
    if rental_type == 'Casual':
        return data[data['casual'] > 0]
    elif rental_type == 'Registered':
        return data[data['registered'] > 0]
    else:
        return data

# Sidebar for user input
st.sidebar.header('Filter Data')
rental_type = st.sidebar.selectbox('Rental Type', ['Casual', 'Registered'])

# Filter data based on user input
filtered_data = filter_data(combined_data, rental_type)

# Group data by weather situation and calculate total rentals
rentals_by_weather = filtered_data.groupby('weathersit')['cnt'].sum().reset_index()

# Plotting bar chart for rentals by weather conditions
st.subheader('Total Rentals by Weather Conditions')
plt.figure(figsize=(10, 6))
sns.barplot(x='weathersit', y='cnt', data=rentals_by_weather)
plt.title('Total Rentals by Weather Conditions')
plt.xlabel('Weather Conditions')
plt.ylabel('Total Rentals')
st.pyplot(plt)

# Group data by month and calculate total rentals
rentals_by_month = filtered_data.groupby('mnth')['cnt'].sum().reset_index()

# Plotting bar chart for rentals by month
st.subheader('Total Rentals by Month')
plt.figure(figsize=(10, 6))
sns.barplot(x='mnth', y='cnt', data=rentals_by_month)
plt.title('Total Rentals by Month')
plt.xlabel('Month')
plt.ylabel('Total Rentals')
st.pyplot(plt)

# Plotting line chart for monthly rentals from prediction data
st.subheader('Rentals Prediction')
plt.figure(figsize=(24, 10))
sns.lineplot(x=prediction_data['mnth'], y=prediction_data['cnt'], marker='o', linestyle='-')
plt.xlabel('Month')
plt.ylabel('Number of Rentals')
plt.title('Rental Predictions')
plt.xticks(range(26), prediction_data['mnth'], rotation=45)
plt.grid(True)  # Show grid
plt.plot([24, 25], prediction_data['cnt'].iloc[-2:], marker='o', color='red')

plt.tight_layout()
st.pyplot(plt)

# I don't know what's wrong, but the y-axis doesn't start from the minimum value to the maximum value :(