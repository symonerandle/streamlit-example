import streamlit as st
import pandas as pd

"""
This is my streamlit app.
"""
df = pd.read_csv("data/reddit_comments.csv")
st.dataframe(df)