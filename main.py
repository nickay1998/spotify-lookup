import streamlit as st
from spotify import authenticate_spotify, search_spotify
from streamlit import session_state as ss

st.set_page_config(page_title="Spotify Analysis", layout="wide", initial_sidebar_state="collapsed")

authenticate_spotify()

st.write('# Spotify Lookup')

search_text = st.text_input('Search', key='search_text', placeholder='Search for an artist, album or track!')

if search_text != '':
    search_json = search_spotify()