import streamlit as st
import pandas as pd

"""
This is my streamlit app.
"""

@st.experimental_memo
def load_data():
    return pd.read_csv("data/reddit_comments.csv")
    
df = load_data()
st.dataframe(df)