import pandas as pd 
import csv 
import sys
import random
from argparse import ArgumentParser
import collections
import time

class AppUser:
    """Stores username, favorite genres, and playlists"""
    
    def __init__(self, username):
        self.username = username
        
        #collect user's top 3 favorite genres to build playlists from
        self.fav_genres = []
        
        #key is playlist name, value is list of song name
        self.playlists = {}
   
class MusicApp:
    """A music selection app with a library of songs that can create new app users, 
    create playlists for those users, and allows users to name the playlist"""

    def __init__(self):
        self.catelog = pd.read_csv('Musiclist_326_project.csv')
        
        #key value pair of usernames and user objects
        self.users = collections.defaultdict(AppUser)
        self.cur_user = None
        self.genres = self.catelog['genre'].unique()
        
        #welcome message
        print("Welcome to MusicApp!\n")

    def createNewUser(self, username):
        """Create a new user for our MusicApp and asks user for their favorite genres"""
        
        new_user = AppUser(username)
        
        self.users[username] = new_user
        
        print("Welcome, " + username + "!\n")
        print("Please choose your 3 favorite genres")
        print("Here are your options:")
        
        print(self.genres)
        
        mod = ["first ", "second ", "third "]
        mod_ind = 0
        
        while mod_ind < 3:
            cur_genre = str(input("Enter your " + mod[mod_ind] + "favorite genre: "))
            if cur_genre not in self.genres:
                print("Sorry, please enter a valid genre")
                continue
            else:
                new_user.fav_genres.append(cur_genre)
                mod_ind += 1

        return new_user   
    
    def create_playlist(self, cur_user):
        """Create up to 5 random playlists of 15 songs based on one of the user's
        favorite genres, 5 from each genre"""
        
        if len(cur_user.playlists) > 4:
            print("Maximum number of playlists reached")
            return

        playlist_name = input("Give your playlist a name: ")
        
        print("Here are your favorite genres: " + str(cur_user.fav_genres))
        
        playlist = []
        
        for g in cur_user.fav_genres:
            genre_songs = self.catelog[self.catelog['genre'] == g]
            genre_songs = genre_songs[['genre', 'artist_name', 'track_name']]
            picks = genre_songs.sample(n=5)
            playlist.append(picks)
            
        playlist = pd.concat(playlist)
        
        print("This is your playlist!")
        print(playlist)
        
        cur_user.playlists[playlist_name] = playlist
        
    def choose_playlist(self, cur_user):
        """Choose which playlist you want to play"""
        print(list(cur_user.playlists.keys()))
        
        while True:
            name = input("Pick a playlist: ")
            if name not in cur_user.playlists:
                print("Please enter a valid playlist")
                continue
            else:
                print('found')
                cur_playlist = cur_user.playlists[name]
                cur_playlist = cur_playlist.values.tolist()
                for genre, artist, track in cur_playlist:
                    print(f"Now playing {track} by {artist}... ")
                    time.sleep(0.5)
                break
    
def main():
    myMusicApp = MusicApp()
    
    user_name = str(input("To create an account, please enter a username: "))

    cur_user = myMusicApp.createNewUser(user_name)

    choice = ''
    
    #Start a loop that runs until the user enters the value for 'quit'.
    while choice != 'q':
        print(f"OK, {cur_user.username}. What would you like to do?")
        
        #print all choices in a series of print statements
        print("[1] Enter 1 to create a random playlist based on your favorite genres")
        print("[2] Enter 2 to choose a playlist to play!")
        print("[q] Enter q to quit.")

        choice = input("Enter your choice: ")
        
        if choice == '1':
            myMusicApp.create_playlist(cur_user)
        elif choice == '2':
            myMusicApp.choose_playlist(cur_user)
        elif choice == 'q':
            print('Thanks for stopping by!')
            
if __name__ == "__main__":
    main()
            
    class suggestsearch:
        
        def __init__(self):
            self.catelog = pd.read_csv('Musiclist_326_project.csv')
            self.searched = []
        def suggest(self):
            """ The user enters an artist's name and the function returns that artist's more popular songs.  """

            artist_name = input('Please enter the name of the artist you want to listen to')
            df = self.catelog 
            filters = df['popularity'] > 50        #evaluates to True for all songs with popularity > 50
            popular_songs = df[filters]
            col = df[artist_name, 'track_name']
            songs = popular_songs[col]
            return songs
            
            with open('Musiclist_326_projects.csv') as f:
                spreadsheet = csv.DictReader(f)
                for row in spreadsheet:
                    if self.artist in row['artist_name']:
                        if row['popularity'] > 50:
                            print(row['track_name'])
    
        def search(self):
            """This funtion """
            df = self.catelog
            aort = input("Artist or Title (A for artist, T for title)")
            if aort == "T":
                track_name = input("Please enter a track name")
                self.searched.append(track_name)
                song = df[df['track_name'] == track_name]
                return song
            if aort == "A":
                artist_name = input("Please enter a artist name")
                self.searched.append(artist_name)
                artist = df[df['artist_name'] == artist_name]
                return artist
            
        def recently_searched(self):
            """Organizes list that is in suggest function to show the most recently searched artists. 
                Will return the list with the most recent in the 0 position."""
            recent_search = self.searched[::-1]
            if len(recent_search) > 10:
                del self.searched[10:]
            return recent_search
    



    
    
