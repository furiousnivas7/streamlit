import streamlit as st
import datetime
import pandas as pd

st.write("Vanakam Ashon")

# Input fields
firstname = st.text_input("Firstname", placeholder="Enter your first name", max_chars=10)
secondname = st.text_input("Secondname", placeholder="Enter your second name", max_chars=10)
birthday = st.date_input("When's your birthday", datetime.date(2019, 7, 6))
button = st.button('Submit')
# Button to submit data
if button:
    # Creating a DataFrame to display the data in a table format
    data = {
        "Firstname": [firstname],
        "Secondname": [secondname],
        "Birthday": [birthday]
    }
    df = pd.DataFrame(data)
    
    # Display the DataFrame
    st.table(df)
