#find a database with a list of songs to import from then replace the line below
import pandas as pd 
import csv 
import sys
import random
from argparse import ArgumentParser



def Musiclist_326_project.csv(csv, song):
    """ This method reads a CSV file containing the different kind of songs and other information that goes along with it.
    Args:
        csv (str): a string that allows the csv file to be read.
        song (str): the type of song you are looking for (song, genre, etc)  
    Returns:
        A DataFrame that displays songs that match your prefrence.
    """
    
    pd.set_option('display.max_rows', None)
    """ makes a table based on genre,etc.."""
    df = pd.read_csv(csv)
    print(df[df["song"]== song])
    
class MusicApp:
    """ A music selection app similar to Spotify. 
        Creates/plays playlist based on user's mood.
        Create artist profiles that includes their music sorted by album release dates which users can listen to.
        
        
        Attributes:
        playlist(list of songs): a list of songs
        genre(list of genre): a list of genres
        artist(list of artist): a list of artists
        
    """

    def createUser():
        """Setting up user account """
        user = input(print("Create a Username: "))
        pw = input(print("Create a password: "))
        

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

    def createUser():
        """Setting up user account """
      

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
        """Organizes list that is in suggest function to show the most recently searched artists. 
           Will return the list with the most recent in the 0 position."""
        recent_search = searched[::-1]
        if len(recent_search) > 10:
            del searched[10:]
        return recent_search
    


   
def parse_args(arglist):
    """ Parse command-line arguments """
    parser = ArgumentParser()
    parser.add_argument("csv", help="the path to the csv file")
    parser.add_argument(" ", help="the type of song you want to find")
    return parser.parse_args(arglist)


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    movie_database(args.csv, args.song )
    
    
