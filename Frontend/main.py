import streamlit as st
import requests
import os

# Base URL for the FastAPI backend
# Make sure your FastAPI app is running on this address
BASE_URL = os.getenv("BACKEND-URL", "http://localhost:8000")

st.title("FastAPI API Client")
st.write("A simple UI to test our backend endpoints.")

st.markdown("---")

# ---------------------------------------------------------
# 1. Root Endpoint
# ---------------------------------------------------------
st.header("1. Root Endpoint (`/`)")
st.write("Fetches the welcome message.")

if st.button("Call Root API", key="root_btn"):
    with st.spinner("Calling API..."):
        try:
            response = requests.get(f"{BASE_URL}/")
            response.raise_for_status() # Raise an exception for bad status codes
            st.success("Success!")
            st.json(response.json())
        except requests.exceptions.RequestException as e:
            st.error(f"Error connecting to API: {e}")

st.markdown("---")

# ---------------------------------------------------------
# 2. Maker Endpoint
# ---------------------------------------------------------
st.header("2. Maker Endpoint (`/maker`)")
st.write("Fetches information about the creator.")

if st.button("Call Maker API", key="maker_btn"):
    with st.spinner("Calling API..."):
        try:
            response = requests.get(f"{BASE_URL}/maker")
            response.raise_for_status()
            st.success("Success!")
            st.json(response.json())
        except requests.exceptions.RequestException as e:
            st.error(f"Error connecting to API: {e}")

st.markdown("---")

# ---------------------------------------------------------
# 3. WhoAmI Endpoint
# ---------------------------------------------------------
st.header("3. WhoAmI Endpoint (`/who`)")
st.write("Fetches container and instance metadata.")

if st.button("Call WhoAmI API", key="who_btn"):
    with st.spinner("Calling API..."):
        try:
            response = requests.get(f"{BASE_URL}/who")
            response.raise_for_status()
            st.success("Success!")
            st.json(response.json())
        except requests.exceptions.RequestException as e:
            st.error(f"Error connecting to API: {e}")