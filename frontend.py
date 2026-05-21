import streamlit as st
import requests

Api_url = "http://127.0.0.1:8000/predict"

st.title("Insurance Premium category Predictior")

st.markdown("Enter your details below :")

age = st.number_input("Age",min_value)