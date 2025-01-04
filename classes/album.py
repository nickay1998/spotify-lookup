import streamlit as st
from classes import Artist

class Album:
    def __init__(self, json):
        self.url = json['external_urls']['spotify']

        self.total_tracks = json['total_tracks']
        self.available_markets = json['available_markets']
        self.href = json['href']
        self.images = json['images']
        self.name = json['name']
        self.release_date = json['release_date']
        self.uri = json['uri']
        self.artist = [Artist(item, True) for item in json['artists']]

def parse_album_json(json):
    albums = []
    
    if 'albums' not in json or len(json['albums']['items']) == 0:
        return []
    
    items = json['albums']['items']

    st.write(f'Total items: {len(items)}')

    for item in items:
        album = Album(item)
        albums.append(album)

    return albums