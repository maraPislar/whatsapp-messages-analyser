import streamlit as st
from PIL import Image
import datetime

st.set_page_config(page_title="Bună dimineața!", page_icon=":sunrise:")

st.container()

st.markdown("<h1 style='text-align: center; color: #FFD700;'>Bună dimineața! ☀️</h1>", unsafe_allow_html=True)

now = datetime.datetime.now()

st.markdown(f"<p style='text-align: left; color: #050d14;'>Te-ai trezit la {now.strftime('%H:%M')}!</p>", unsafe_allow_html=True)

image = Image.open('sunrise.jpg')  # Replace with your image path
st.image(image, caption='A beautiful sunrise', use_column_width=True)

st.markdown("""
<style>
.stApp {
    background-color: #F0F8FF; /* Light blue background */
    font-family: 'Arial', sans-serif;
}
</style>
""", unsafe_allow_html=True)