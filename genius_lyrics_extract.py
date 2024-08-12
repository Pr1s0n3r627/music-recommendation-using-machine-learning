
'''
# List of Spotify track URLs
track_urls = [
    "https://open.spotify.com/track/6K4t31amVTZDgR3sKmwUJJ",
    "https://open.spotify.com/track/42VsgItocQwOQC3XWZ8JNA",
    "https://open.spotify.com/track/63OQupATfueTdZMWTxW03A",
    "https://open.spotify.com/track/7y8X0Z04gJCKtfrnSAMywJ",
    "https://open.spotify.com/track/10nyNJ6zNy2YVYLrcwLccB",
    "https://open.spotify.com/track/2tudvzsrR56uom6smgOcSf",
    "https://open.spotify.com/track/70LcF31zb1H0PyJoS1Sx1r",
    "https://open.spotify.com/track/2rtGaCAeYtmcIvuZsvgTf6",
    "https://open.spotify.com/track/3vkCueOmm7xQDoJ17W1Pm3",
    "https://open.spotify.com/track/3xby7fOyqmeON8jsnom0AT",
    "https://open.spotify.com/track/2Hh3ETdQKrmSI3QS0hme7g",
    "https://open.spotify.com/track/5M4yti0QxgqJieUYaEXcpw",
    "https://open.spotify.com/track/2X485T9Z5Ly0xyaghN73ed",
    "https://open.spotify.com/track/50HCj9kEXIonBwRLXFWCr8",
    "https://open.spotify.com/track/6IZvVAP7VPPnsGX6bvgkqg",
    "https://open.spotify.com/track/4OmfWzukSVD140NiAIEjem",
    "https://open.spotify.com/track/1hz7SRTGUNAtIQ46qiNv2p",
    "https://open.spotify.com/track/3DK6m7It6Pw857FcQftMds",
    "https://open.spotify.com/track/7rbECVPkY5UODxoOUVKZnA",
    "https://open.spotify.com/track/5TRPicyLGbAF2LGBFbHGvO",
    "https://open.spotify.com/track/4KW1lqgSr8TKrvBII0Brf8",
    "https://open.spotify.com/track/1UGD3lW3tDmgZfAVDh6w7r",
    "https://open.spotify.com/track/3s7MCdXyWmwjdcWh7GWXas",
    "https://open.spotify.com/track/51EC3I1nQXpec4gDk0mQyP",
    "https://open.spotify.com/track/3sNVsP50132BTNlImLx70i",
    "https://open.spotify.com/track/0fv2KH6hac06J86hBUTcSf",
    "https://open.spotify.com/track/5QvBXUm5MglLJ3iBfTX2Wo",
    "https://open.spotify.com/track/3xKsf9qdS1CyvXSMEid6g8",
    "https://open.spotify.com/track/6BU1RZexmvJcBjgagVVt3M",
    "https://open.spotify.com/track/0NrtwAmRAdLxua31SzHvXr",
    "https://open.spotify.com/track/0y9uTzK9cNKSAEHnpeRG8C",
    "https://open.spotify.com/track/3EG9FJ0ToLfgnc1IG2Z1wz",
    "https://open.spotify.com/track/6rqj2zeKhLy3exkuFi6mSz",
    "https://open.spotify.com/track/5KUNwkaNf8l5A9sXZhiCgI",
    "https://open.spotify.com/track/4gh0ZnHzaTMT1sDga7Ek0N",
    "https://open.spotify.com/track/52ojopYMUzeNcudsoz7O9D",
    "https://open.spotify.com/track/6NMtzpDQBTOfJwMzgMX0zl",
    "https://open.spotify.com/track/7umZiitjVsEjMQ6HNddpUI",
    "https://open.spotify.com/track/0NjW4SKY3gbfl2orl1p8hr",
    "https://open.spotify.com/track/1gT5TGwbkkkUliNzHRIGi1",
    "https://open.spotify.com/track/2R4AlwtrrkMaRKojcTIzmL",
    "https://open.spotify.com/track/2aPTvyE09vUCRwVvj0I8WK",
    "https://open.spotify.com/track/4QhWbupniDd44EDtnh2bFJ",
    "https://open.spotify.com/track/2gAGWaK4wvt2xrFUlR4mK8",
    "https://open.spotify.com/track/4b82tXj35SycILuILcgBQ6",
    "https://open.spotify.com/track/6FBzhcfgGacfXF3AmtfEaX",
    "https://open.spotify.com/track/1nXZnTALNXiPlvXotqHm66",
    "https://open.spotify.com/track/0zLClc0emc6qUeV1p5nc99",
    "https://open.spotify.com/track/4f8Mh5wuWHOsfXtzjrJB3t",
    "https://open.spotify.com/track/1gqkRc9WtOpnGIqxf2Hvzr"
    # Add more URLs here
]
'''


import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import requests
from bs4 import BeautifulSoup
import csv

# Spotify API setup
SPOTIPY_CLIENT_ID = 'b5c0897934bb4ff88e02873ac439a747'
SPOTIPY_CLIENT_SECRET = '5b89506754c94b1582d9cd19d4b0fe9e'

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID,
                                                           client_secret=SPOTIPY_CLIENT_SECRET))

# Function to search for lyrics on Genius
def get_lyrics_from_genius(artist, title):
    base_url = "https://genius.com"
    search_url = f"{base_url}/search?q={artist} {title}"
    response = requests.get(search_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find the first link to a song page
    song_link = soup.find('a', class_='mini_card')
    if song_link:
        song_url = song_link['href']
        song_page = requests.get(song_url)
        song_soup = BeautifulSoup(song_page.text, 'html.parser')
        lyrics_div = song_soup.find('div', class_='lyrics')
        
        # Lyrics may be in another div if the 'lyrics' div is not present
        if not lyrics_div:
            lyrics_div = song_soup.find('div', class_='Lyrics__Container-sc-1ynbvzw-6')
        
        if lyrics_div:
            return lyrics_div.get_text(separator="\n")
    
    return "Lyrics not found"

# List of Spotify track URLs
track_urls = [
    "https://open.spotify.com/track/6K4t31amVTZDgR3sKmwUJJ",
    "https://open.spotify.com/track/42VsgItocQwOQC3XWZ8JNA",
    "https://open.spotify.com/track/63OQupATfueTdZMWTxW03A",
    "https://open.spotify.com/track/7y8X0Z04gJCKtfrnSAMywJ",
    "https://open.spotify.com/track/10nyNJ6zNy2YVYLrcwLccB",
    "https://open.spotify.com/track/2tudvzsrR56uom6smgOcSf",
    "https://open.spotify.com/track/70LcF31zb1H0PyJoS1Sx1r",
    "https://open.spotify.com/track/2rtGaCAeYtmcIvuZsvgTf6",
    "https://open.spotify.com/track/3vkCueOmm7xQDoJ17W1Pm3",
    "https://open.spotify.com/track/3xby7fOyqmeON8jsnom0AT",
    "https://open.spotify.com/track/2Hh3ETdQKrmSI3QS0hme7g",
    "https://open.spotify.com/track/5M4yti0QxgqJieUYaEXcpw",
    "https://open.spotify.com/track/2X485T9Z5Ly0xyaghN73ed",
    "https://open.spotify.com/track/50HCj9kEXIonBwRLXFWCr8",
    "https://open.spotify.com/track/6IZvVAP7VPPnsGX6bvgkqg",
    "https://open.spotify.com/track/4OmfWzukSVD140NiAIEjem",
    "https://open.spotify.com/track/1hz7SRTGUNAtIQ46qiNv2p",
    "https://open.spotify.com/track/3DK6m7It6Pw857FcQftMds",
    "https://open.spotify.com/track/7rbECVPkY5UODxoOUVKZnA",
    "https://open.spotify.com/track/5TRPicyLGbAF2LGBFbHGvO",
    "https://open.spotify.com/track/4KW1lqgSr8TKrvBII0Brf8",
    "https://open.spotify.com/track/1UGD3lW3tDmgZfAVDh6w7r",
    "https://open.spotify.com/track/3s7MCdXyWmwjdcWh7GWXas",
    "https://open.spotify.com/track/51EC3I1nQXpec4gDk0mQyP",
    "https://open.spotify.com/track/3sNVsP50132BTNlImLx70i",
    "https://open.spotify.com/track/0fv2KH6hac06J86hBUTcSf",
    "https://open.spotify.com/track/5QvBXUm5MglLJ3iBfTX2Wo",
    "https://open.spotify.com/track/3xKsf9qdS1CyvXSMEid6g8",
    "https://open.spotify.com/track/6BU1RZexmvJcBjgagVVt3M",
    "https://open.spotify.com/track/0NrtwAmRAdLxua31SzHvXr",
    "https://open.spotify.com/track/0y9uTzK9cNKSAEHnpeRG8C",
    "https://open.spotify.com/track/3EG9FJ0ToLfgnc1IG2Z1wz",
    "https://open.spotify.com/track/6rqj2zeKhLy3exkuFi6mSz",
    "https://open.spotify.com/track/5KUNwkaNf8l5A9sXZhiCgI",
    "https://open.spotify.com/track/4gh0ZnHzaTMT1sDga7Ek0N",
    "https://open.spotify.com/track/52ojopYMUzeNcudsoz7O9D",
    "https://open.spotify.com/track/6NMtzpDQBTOfJwMzgMX0zl",
    "https://open.spotify.com/track/7umZiitjVsEjMQ6HNddpUI",
    "https://open.spotify.com/track/0NjW4SKY3gbfl2orl1p8hr",
    "https://open.spotify.com/track/1gT5TGwbkkkUliNzHRIGi1",
    "https://open.spotify.com/track/2R4AlwtrrkMaRKojcTIzmL",
    "https://open.spotify.com/track/2aPTvyE09vUCRwVvj0I8WK",
    "https://open.spotify.com/track/4QhWbupniDd44EDtnh2bFJ",
    "https://open.spotify.com/track/2gAGWaK4wvt2xrFUlR4mK8",
    "https://open.spotify.com/track/4b82tXj35SycILuILcgBQ6",
    "https://open.spotify.com/track/6FBzhcfgGacfXF3AmtfEaX",
    "https://open.spotify.com/track/1nXZnTALNXiPlvXotqHm66",
    "https://open.spotify.com/track/0zLClc0emc6qUeV1p5nc99",
    "https://open.spotify.com/track/4f8Mh5wuWHOsfXtzjrJB3t",
    "https://open.spotify.com/track/1gqkRc9WtOpnGIqxf2Hvzr"
    # Add more URLs here
]

# Open the CSV file in write mode once
with open('small_songdata.csv', 'w', newline='', encoding='utf-8') as csvfile:
    # Create a CSV writer object
    writer = csv.writer(csvfile)
    
    # Write the header row
    writer.writerow(['track_name', 'artist_name', 'lyrics'])
    
    # Loop through each track URL and fetch lyrics
    for url in track_urls:
        try:
            track_id = url.split("/")[-1]
            track_info = sp.track(track_id)
            artist_name = track_info['artists'][0]['name']
            track_name = track_info['name']
            
            print(f"Fetching lyrics for {track_name} by {artist_name}...")
            lyrics = get_lyrics_from_genius(artist_name, track_name)
            
            print(f"Lyrics for {track_name}:\n{lyrics}\n")
            
            # Write the track information and lyrics to the CSV file
            writer.writerow([track_name, artist_name, lyrics])
        
        except Exception as e:
            print(f"Error fetching data for URL {url}: {e}")

print('----- Data extraction is complete. Check the CSV file. -----')
