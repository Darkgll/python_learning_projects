from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

date_choice = input("Which year do you want to travel to? Type the data in this format YYYY-MM-DD")

# find songs on www.billboard.com
site_to_soap = f"https://www.billboard.com/charts/hot-100/{date_choice}"
print(site_to_soap)
response = requests.get(site_to_soap)
response_text = response.text

soap = BeautifulSoup(response_text, "html.parser")
cl = "chart-element__information__song"
soap_songs = soap.find_all(name="span", class_=cl)

songs = []
for tag in soap_songs:
    song = tag.getText()
    songs.append(song)
    print(song)
print(songs)

# Spotify authorisation
cl_id = None  # YOUR CLIENT ID
cl_s = None  # YOUR SECRET CODE
red_uri = None  # "http://example.com"
us_name = None  # YOUR USER NAME

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=cl_id, client_secret=cl_s, redirect_uri=red_uri, scope="playlist-modify-private",
    username=us_name))

user_id = sp.current_user()['id']

song_iri_list = []
year = date_choice.split('-')[0]
for song in songs:
    result = sp.search(q=f'track:{song} year:{year}', type="track")
    try:
        song_uri = result['tracks']['items'][0]['uri']
        song_iri_list.append(song_uri)
    except IndexError:
        print(f"Can't find this {song} on Spotify.")
print(song_iri_list)

playlist_name = f"{date_choice} Billboard 100"

make_playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=False)
print(make_playlist)
playlist_id = make_playlist['id']

add_tracks = sp.playlist_add_items(playlist_id=playlist_id, items=song_iri_list)
