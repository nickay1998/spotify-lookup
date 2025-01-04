import streamlit as st
from spotify import authenticate_spotify
from streamlit import session_state as ss

authenticate_spotify()

st.write(f'Connect to spotify API! Token: \'{ss["token"]}\'')