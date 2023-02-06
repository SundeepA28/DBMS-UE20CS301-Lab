import datetime

import pandas as pd
import streamlit as st
from database import view_all_data, view_only_dealer_names, get_dealer, edit_dealer_data


def update():
    result = view_all_data()
    # st.write(result)
    df = pd.DataFrame(result, columns=['Train_id','Train_name','Train_type', 'Source', 'Destination','Availability'])
    with st.expander("Current Trains"):
        st.dataframe(df)
    list_of_Trains = [i[0] for i in view_only_dealer_names()]
    selected_train = st.selectbox("Trains to Edit", list_of_Trains)
    selected_result = get_dealer(selected_train)
    # st.write(selected_result)
    if selected_result:
        Train_id = selected_result[0][0]
        Train_name = selected_result[0][1]
        Train_type = selected_result[0][2]
        Source = selected_result[0][3]
        Destination = selected_result[0][4]
        Availability = selected_result[0][5]

        # Layout of Create

        col1, col2 = st.columns(2)
        with col1:
            new_Train_id = st.text_input("ID:", Train_id)
            new_Train_name = st.text_input("Name:", Train_name)
        with col2:
            new_Train_type = st.selectbox(Train_type, ["Superfast", "Fast", "Mail"])
            new_Source = st.text_input("Source:", Source)
        new_Destination = st.text_input("Destination:", Destination)
        new_Availability = st.text_input("Availability:", Availability)
        if st.button("Update Train"):
            edit_dealer_data(new_Train_id,new_Train_name,new_Train_type, new_Source, new_Destination,new_Availability,Train_id, Train_name, Train_type, Source, Destination,Availability)
            st.success("Successfully updated:: {} to ::{}".format(Availability, new_Availability))

    result2 = view_all_data()
    df2 = pd.DataFrame(result2, columns=['Train_id','Train_name','Train_type', 'Source', 'Destination','Availability'])
    with st.expander("Updated data"):
        st.dataframe(df2)
