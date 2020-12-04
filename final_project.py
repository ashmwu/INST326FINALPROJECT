#find a database with a list of songs to import from then replace the line below
<<<<<<< HEAD
import playlist from database

import csv 


=======
import pandas as pd
>>>>>>> e17ccdf91452e7d30a88850e3364dc65c7491795
class MusicApp:
    """ A music selection app similar to Spotify. 
        Creates/plays playlist based on user's mood.
        Create artist profiles that includes their music sorted by album release dates which users can listen to.
        
        
        Attributes:
            
    """
    def __init__(self, genre, artist):
        """ initialize variables that we need
            Will change as we work on code
        """
        self.genre = genre 
        self. artist = artist 
        mood = [happy, sad, angry, frusterated, jealously, heartbreak, excited]
        artist = [Ariana Grande, BTS, Justin Bieber, Pop Smoke]
        genre = [EDM, Pop, Rap, Lo-fi, K-Pop, Country, Indie]
    def mood():
        """Select a mood to be able to get a list of songs that match the mood. """
    def shuffle():
        """ Randomly shuffles the music"""
<<<<<<< HEAD
    def function():
        """ """
    def function2():
        """ """
    def suggest(self, genre, artist):
        """ The user enters an artist's name and the function returns that artist's more popular songs.  """
        
        with open('Musiclist_326_projects.csv') as f:
            spreadsheet = csv.Dictreader(f)
            for row in spreadsheet:
                if row['popularity'] > 50:
                    print(row['genre'],row['artist_name'])
                
                    
        
        
        
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
<<<<<<< HEAD
    def lyrics():
        """Will pull up the lyrics of a song"""
    def 
    
=======
    def search():
        """Searches for the song"""
        
    def recently_searched():
        """Creates a list of the ten most recently played songs."""
        searched = []
        #
        searched.append[]
        recent_search = searched[::-1]
        reversed_list = systems[::-1]
        if len(recent_search) > 10:
            del searched[11:]
        return recent_search
>>>>>>> e17ccdf91452e7d30a88850e3364dc65c7491795
        