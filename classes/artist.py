import streamlit as st

class Artist:
    def __init__(self, json, album=False):
        self.url = json['external_urls']['spotify']
        self.href = json['href']
        self.uri = json['uri']
        self.name = json['name']

        if album:
            return

        self.followers = json['followers']['total']
        self.genres = json['genres']
        self.images = json['images']
        self.popularity = json['popularity']
        

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