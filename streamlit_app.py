import streamlit as st
import pandas as pd

"""
This is my streamlit app.
"""

@st.experimental_memo(show_spinner=True)
def load_data():
    return pd.read_csv("data/reddit_comments.csv")

def hide_data():
    return st.button("Show grid", on_click=load_data())

df = load_data()
st.dataframe(df)

st.button("close grid", on_click=hide_data())
