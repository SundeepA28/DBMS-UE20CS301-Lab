import streamlit as st
from database import add_data


def create():
    col1, col2 = st.columns(2)
    with col1:
        Train_id = st.text_input("Train_No")
        Train_name = st.text_input("Name:")
    with col2:
        Train_type = st.selectbox("Type: ", ["Superfast", "Fast", "Mail"])
        Source = st.text_input("Source: ")
        Destination = st.text_input("Destination: ")
        Availability = st.text_input("Availability :")
    if st.button("Add Train Details"):
        add_data(Train_id,Train_name, Train_type, Source, Destination,Availability)
        st.success("Successfully added Train: {}".format(Train_name))
