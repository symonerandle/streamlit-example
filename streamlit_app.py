import streamlit as st
import pandas as pd

"""
This is my streamlit app.
"""

@st.experimental_memo
def load_data():
    tab1, tab2 = st.tabs(["Tab 1", "Tab2"])
    with tab1:
        pd.read_csv("data/reddit_comments.csv")
    return
df = load_data()
st.dataframe(df)

st.button("close grid")