import streamlit as st
import datetime
st.write("vanakam ashon")
firstname=st.text_input("firstname","enter your first name")
secondname=st.text_input("secondname","enter your second name")
d = st.date_input("When's your birthday", datetime.date(2019, 7, 6))
# st.write('Your birthday is:', d)
