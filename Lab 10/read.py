import pandas as pd
import streamlit as st
import plotly.express as px
from database import view_all_data


def read():
    result = view_all_data()
    df = pd.DataFrame(result, columns=['Train_id','Train_name','Train_type','Source','Destination','Availability'])
    with st.expander("View all Trains"):
        st.dataframe(df)
    # with st.expander("Dealer Location"):
    #     task_df = df['Train_type'].value_counts().to_frame()
    #     task_df = task_df.reset_index()
    #     st.dataframe(task_df)
    #     p1 = px.pie(task_df, names='index', values='Train type')
    #     st.plotly_chart(p1)