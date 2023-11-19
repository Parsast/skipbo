import requests
import json
import pandas as pd
import csv
import schedule
import time

def get_spotify_token(client_id, client_secret):
    # Get the access token from Spotify
    auth_response = requests.post(
        'https://accounts.spotify.com/api/token',
        {
            'grant_type': 'client_credentials',
            'client_id': client_id,
            'client_secret': client_secret,
        }
    )
    auth_response_data = auth_response.json()
    
    return auth_response_data['access_token']

def get_markets(access_token):
    response = requests.get('https://api.spotify.com/v1/markets',
    headers = {
        'Authorization':f'Bearer {access_token}'
        }
    )
    data = response.json()
    return data["markets"]
def get_top_tracks_Allcountries(artist_Spotify_Id, access_token):
    markets = get_markets(access_token)
    top_tracks = dict()
    for market in markets:
        response = requests.get(f'https://api.spotify.com/v1/artists/5b1CDxqOGnXr5M1DUn2XQh/top-tracks?market={market}',
        headers = {
         'Authorization':f'Bearer {access_token}'
        }
        )
        # print(type(response.json()))
        tracks = response.json()["tracks"]
        
        for track in tracks:
            if track["id"] in top_tracks.keys():
                top_tracks[track["id"]][market] = 1
            else:
                top_tracks[track["id"]] = dict()
                top_tracks[track["id"]][market] = 1
                for key in track.keys():
                    if isinstance(track[key] ,str) or isinstance(track[key] ,int):
                        top_tracks[track["id"]][key] = track[key]

    return top_tracks

def get_audio_analysis(trackId,access_token):
    response = requests.get(f'https://api.spotify.com/v1/audio-analysis/{trackId}',
    headers = {
         'Authorization':f'Bearer {access_token}'
        }
    )
    response = response.json()
    return response

client_id = ''
client_secret = ''
access_token = get_spotify_token(client_id,client_secret)

trackId = "3eXw9bwtqRmiEs5Su7UMTG" 
response = get_audio_analysis(trackId,access_token)
print(str(response["meta"]))   
# print(str(top_tracks["2qhO9ssQR1ydJmWJGaQz58"].keys()))

# Hayedeh = "5b1CDxqOGnXr5M1DUn2XQh"
# top_tracks = get_top_tracks_Allcountries(Hayedeh, token)
# print(str(top_tracks))

# with open('data.json', "w") as j:
#     json.dump(top_tracks, j)

# with open('data.json','r') as r:
#     top_tracks_json = json.load(r)

# data = pd.read_json(top_tracks)
# flattened_data = pd.json_normalize(data)
# with open('data.json', "w") as j:
#     json.dump(top_tracks, j)
# with open('hayedeh.csv','w', newline='') as file:
#     fieldnames = top_tracks[next(iter(top_tracks))].keys()
#     writer = csv.DictWriter(file, fieldnames=fieldnames)

#     writer.writeheader()

#     for key in top_tracks:
#         writer.writerow(top_tracks[key])
# flattened_data.to_csv('flattened_data.csv', index=False)
