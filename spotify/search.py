import streamlit as st
from streamlit import session_state as ss
from utils import get_data
from classes import parse_artist_json, parse_album_json, parse_track_json
import math

def search_spotify():
    limit = 50
    
    search_text = ss['search_text']
    search_text = search_text.replace(" ", "+")

    if 'previous_search_text' in ss and search_text == ss['previous_search_text']:
        return ss['previous_search_json']
    
    with st.spinner('Searching spotify...'):
        search_json = search(search_text)

    ss['previous_search_text'] = search_text
    ss['previous_search_json'] = search_json

    artist_tab, album_tab, track_tab = st.tabs(['Artists', 'Albums', 'Tracks'])

    with artist_tab:
        artists = parse_artist_json(search_json)
        
        for artist in artists:
            st.write(artist.name)
    with album_tab:
        albums = parse_album_json(search_json)

        for album in albums:
            st.write(album.name)
    with track_tab:
        tracks = parse_track_json(search_json)

        for track in tracks:
            st.write(track.name)

    return search_json

def search(search_text, limit=50, offset=0):
    url = f"https://api.spotify.com/v1/search?q={search_text}&type=album%2Cartist%2Ctrack&limit={limit}&offset={offset}"
    search_json = get_data(url)

    return search_json