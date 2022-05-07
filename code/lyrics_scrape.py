import requests
import pandas as pd
import os
import lyricsgenius

PATH = os.path.join("..", "data", "spotify_songs.csv")

clienttoken = "rDOZnXwfehsF8xq5eqpK6v9qwO4zPRU9kjqfdW9MtRu9oM1_J1dPv64vZH-2qYxb"

genius = lyricsgenius.Genius(clienttoken)

songlist = pd.read_csv(PATH)

songinfo = songlist.loc[:,["track_name", "track_artist"]]

def get_lyrics(song, artist):
    song = genius.search_song(song, artist)
    if song == None:
        output = ""
    else:
        output = song.lyrics
    return output

lyrics = []

for i in range(len(songinfo)):
    songname = songinfo.loc[i][0]
    songartist = songinfo.loc[i][1]
    
    words = get_lyrics(songname, songartist)
    lyrics += [words]