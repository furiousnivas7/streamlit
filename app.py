import streamlit as st
import datetime
import pandas as pd
import json
import os


st.write("Vanakam Ashon")
json_file_path = 'data.json'

# Function to load data from JSON file
def load_data(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return json.load(file)
    return []

# Function to save data to JSON file
def save_data(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4, default=str)

        
# Load existing data
data = load_data(json_file_path)

# Input fields
firstname = st.text_input("Firstname", placeholder="Enter your first name", max_chars=10)
secondname = st.text_input("Secondname", placeholder="Enter your second name", max_chars=10)
birthday = st.date_input("When's your birthday", datetime.date(2019, 7, 6))
button = st.button('Submit')
# Button to submit data
if button:
    # Creating a DataFrame to display the data in a table format
    new_entry = {
        "Firstname": firstname,
        "Secondname": secondname,
        "Birthday": birthday
    }
    data.append(new_entry)

    save_data(json_file_path, data)
    df = pd.DataFrame(data)
    
    # Display the DataFrame
    st.table(df)
