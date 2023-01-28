import streamlit as st
import pandas as pd

"""
This is my streamlit app.
"""



@st.experimental_memo #(show_spinner=True)
def load_data():
    return pd.read_csv("data/reddit_comments.csv")

df = load_data()
st.dataframe(df)

st.side_bar()

#def hide_data():
    #return st.button("Show grid", on_click=load_data(df))

#def button_check():
#   print("this button works!")

#btn_chk = button_check()

