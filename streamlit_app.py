import streamlit as st
import pandas as pd

"""
This is my streamlit app.
"""

tab1, tab2 = st.tabs(["Tab 1", "Tab2"])

@st.experimental_memo
def load_data():
    return pd.read_csv("data/reddit_comments.csv")

df = load_data()
st.dataframe(df)

st.button("close grid")