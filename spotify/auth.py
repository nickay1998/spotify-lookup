import streamlit as st
from utils import post_data
from streamlit import session_state as ss
from streamlit import secrets as sec

def retrieve_access_token():
    
    url = "https://accounts.spotify.com/api/token"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = {
        "grant_type": "client_credentials",
        "client_id": sec["API_KEY"],
        "client_secret": sec["API_SECRET"]
    }

    access_token_response = post_data(url, headers, data)

    return access_token_response["access_token"]

def authenticate_spotify():    
    if "token" in st.session_state:
        return
    
    token = ss["token"] = retrieve_access_token()
    st.toast(f"Successfully acquired access token: " + token, icon="✅")