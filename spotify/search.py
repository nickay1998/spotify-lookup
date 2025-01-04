import streamlit as st
from streamlit import session_state as ss
from utils import get_data

def search_spotify():    
    search_text = ss['search_text']
    search_text = search_text.replace(" ", "+")

    if 'previous_search_text' in ss and search_text == ss['previous_search_text']:
        return ss['previous_search_json']
    
    with st.spinner('Searching spotify...'):
        url = f"https://api.spotify.com/v1/search?q={search_text}&type=album%2Cartist%2Ctrack"
        search_json = get_data(url)

    ss['previous_search_text'] = search_text
    ss['previous_search_json'] = search_json

    return search_json