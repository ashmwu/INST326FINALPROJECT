import pandas as pd 
import csv 
import sys
import random
from argparse import ArgumentParser
import collections


class AppUser:
    """Stores username, favorite genres, and playlists"""
    
    def __init__(self, username):
        self.username = username
        
        #collect user's top 3 favorite genres to build playlists from
        self.fav_genres = []
        
        #key is playlist name, value is list of song name
        self.playlists = {}
        
        #List for recently_searched to work
        self.searched = []
   
class MusicApp:
    """A music selection app with a library of songs that can create new app users, 
    create playlists for those users, and allows users to name the playlist"""

    def __init__(self):
        self.catelog = pd.read_csv('Musiclist_326_project.csv')
        
        #key value pair of usernames and user objects
        self.users = collections.defaultdict(AppUser)
        self.cur_user = None
        self.genres = self.catelog['genre'].unique()
        self.searched = []
        
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
        
        if not cur_user.playlists:
            print("No playlist found")
            return
        
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
                break
            
    def search(self):
        """This funtion """
        df = self.catelog
        aort = input("Artist or Title (A for artist, T for title): ")
        if aort == "T":
            track_name = input("Please enter a track name: ")
            self.searched.append(track_name)
            song = df[df['track_name'] == track_name]
            song = song[['genre', 'artist_name', 'track_name']]
            print(f"{song}")
            return song
        if aort == "A":
            artist_name = input("Please enter a artist name: ")
            self.searched.append(artist_name)
            artist = df[df['artist_name'] == artist_name]
            artist = artist[['genre', 'artist_name', 'track_name']]
            print(f"{artist}")
            return artist
        
    def recently_searched(self):
            """Organizes list that is in suggest function to show the most recently searched artists. 
                Will return the list with the most recent in the 0 position."""
            recent_search = self.searched[::-1]
            if len(recent_search) == 0:
                print(f"No recently searched")
            if len(recent_search) > 10:
                del recent_search[10:]
            print(f"{recent_search}")
            return recent_search
    
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
        print("[3] Enter 3 to search for a title")
        print("[4] Enter 4 to view search history")
        print("[5] Enter 5 so we can suggest some songs")
        print("[q] Enter q to quit.")

        choice = input("Enter your choice: ")
        
        if choice == '1':
            myMusicApp.create_playlist(cur_user)
        elif choice == '2':
            myMusicApp.choose_playlist(cur_user)
        elif choice == '3':
            myMusicApp.search()
        elif choice == '4':
            myMusicApp.recently_searched()
        elif choice == 'q':
            print('Thanks for stopping by!')
            
if __name__ == "__main__":
    main()
    