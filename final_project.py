#find a database with a list of songs to import from then replace the line below
import pandas as pd 
import csv 
import sys
import random


class MusicApp:
    """ A music selection app similar to Spotify. 
        Creates/plays playlist based on user's mood.
        Create artist profiles that includes their music sorted by album release dates which users can listen to.
        
        
        Attributes:
        playlist(list of songs): a list of songs
        genre(list of genre): a list of genres
        artist(list of artist): a list of artists
        
    """
    searched = []
    def __init__(self, genre, artist, playlist, users):
        """ initialize variables that we need
            Will change as we work on code
        """
        self.genre = genre 
        self.artist = artist 
        self.playlist = playlist
        
    def mood():
        """Select a mood to be able to get a list of songs that match the mood. """
    def shuffle(self):
        """ Randomly shuffles the music in a specific playlist."""
        f = open("Musiclist_326_project.csv", "r")
        playlist.random(f)
        
    def suggest(self):
        """ The user enters an artist's name and the function returns that artist's more popular songs.  """
        
        with open('Musiclist_326_projects.csv') as f:
            spreadsheet = csv.Dictreader(f)
            searched.append[self.artist]
            for row in spreadsheet:
                if self.artist in row['artist_name']:
                    if row['popularity'] > 50:
                        print(row['track_name'])
    def search(self):
        with open('Musiclist_326_projects.csv') as f: 
            
            
        
                    
                
        
=======
    def createUser():
        """Setting up user account """
        
    def suggest():
        """ Based off recent history make music suggestions. Make 
        suggestions based on artist, genre, album """
>>>>>>> e17ccdf91452e7d30a88850e3364dc65c7491795
    def share():
        """Share music currently listening to on social media """
    def library():
        """ This will store all music that has been downloaded to the library"""
        genre = []
        artist = []
        track = []
        with open('Musiclist_326_projects.csv') as f:
            spreadsheet = csv.Dictreader(f)
            for row in spreadsheet:
                if row['genre'] not in genre:
                    genre.append(row['genre'])
                if row['artist_name'] not in artist:
                    artist.append(row['artist_name'])
                track.append(row['track_name'])
                
                
            
    def recently_searched(self):
        """Creates a list of the ten most recently searched artists from suggest function"""
        recent_search = searched[::-1]
        if len(recent_search) > 10:
            del searched[10:]
        return recent_search
    

m = MusicApp()
m.suggest('Rihanna')
        