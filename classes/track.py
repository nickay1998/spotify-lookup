import streamlit as st
from classes import Artist, Album

class Track:
    def __init__(self, json):
        self.url = json['external_urls']['spotify']

        self.available_markets = json['available_markets']
        self.href = json['href']
        self.name = json['name']
        self.uri = json['uri']
        self.artist = [Artist(item, True) for item in json['artists']]
        self.album = Album(json['album'])
        self.duration_ms = json['duration_ms']
        self.explicit = json['explicit']
        self.popularity = json['popularity']

def parse_track_json(json):
    tracks = []
    
    if 'tracks' not in json or len(json['tracks']['items']) == 0:
        return []
    
    items = json['tracks']['items']

    st.write(f'Total items: {len(items)}')

    for item in items:
        track = Track(item)
        tracks.append(track)

    return tracks