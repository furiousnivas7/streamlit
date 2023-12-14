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
download=st.button('Download JSON Data')
# Input fields
firstname = st.text_input("Firstname", placeholder="Enter your first name", max_chars=10)
secondname = st.text_input("Secondname", placeholder="Enter your second name", max_chars=10)
birthday = st.date_input("When's your birthday", datetime.date(2019, 7, 6))
fees_paid = st.radio("Fees Paid", ["Yes", "No"])
last_class_date = st.date_input("Last Class Date", datetime.date.today())
exam_marks = st.number_input("Exam Marks", min_value=0, max_value=100, value=0)
button = st.button('Submit')

# Button to submit data
if button:
    new_entry = {
        "Firstname": firstname,
        "Secondname": secondname,
        "Birthday": birthday,
        "Fees Paid": fees_paid,
        "Last Class Date": last_class_date,
        "Exam Marks": exam_marks
    }
    data.append(new_entry)
    save_data(json_file_path, data)
    df = pd.DataFrame(data)
    
    # Display the DataFrame
    st.table(df)

    # Display bar chart of exam marks
    if len(data) > 0:
        st.bar_chart(df["Exam Marks"])

# Button to download JSON file
if download:
    with open(json_file_path, "r") as file:
        st.download_button(label="Download Data as JSON", data=file, file_name='student_data.json', mime='application/json')

