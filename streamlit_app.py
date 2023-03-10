import streamlit as st
import pandas as pd

#top commit agian
#Container located at top of UI.
con = st.container()
con.write("Inside container")

#Designer function to memorize dataframe display.
#@st.experimental_memo #(show_spinner=True)
def load_data():
    return pd.read_csv("data/reddit_comments.csv")

#Save load_data function into df var. access df in streamlit.
df = load_data()


#expander area
scrbd = st.expander("Score breakdown")
comp = st.expander("Comparison")

scrbd.write("Something")
comp.write("Else")

#st.sidebar.button("Enter", on_click=st.dataframe(df))
#st.text_input()


#def hide_data():
    #return st.button("Show grid", on_click=load_data(df))

#def button_check():
#   print("this button works!")

#btn_chk = button_check()

