import streamlit as st

class Artist:
    def __init__(self, json):
        self.url = json['external_urls']['spotify']
        self.followers = json['followers']['total']
        self.genres = json['genres']
        self.href = json['href']
        self.images = json['images']
        self.name = json['name']
        self.popularity = json['popularity']
        self.uri = json['uri']

def parse_artist_json(json):
    artists = []
    
    if 'artists' not in json or len(json['artists']['items']) == 0:
        return []
    
    items = json['artists']['items']

    st.write(f'Total items: {len(items)}')

    for item in items:
        artist = Artist(item)
        artists.append(artist)

    return artists