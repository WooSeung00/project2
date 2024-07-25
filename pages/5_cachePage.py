import streamlit as st
import time
@st.cache_data
def test():
    time.sleep(5)
    st.write("Hi user.")


test()