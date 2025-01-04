import streamlit as st
from spotify import authenticate_spotify
from streamlit import session_state as ss

st.set_page_config(page_title="Spotify Analysis", layout="wide", initial_sidebar_state="collapsed")

authenticate_spotify()

st.write(f'Connect to spotify API! Token: \'{ss["token"]}\'')