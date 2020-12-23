import pytest
from final_project import MusicApp
from unittest import mock


def test_createNewUser():
    testapp = MusicApp()
    
    with mock.patch("builtins.input", 
                    side_effect=["Rap", "Pop", "Jazz"]):
        user = testapp.createNewUser('bob')
        assert user.username == 'bob'
        assert user.fav_genres == ["Rap", "Pop", "Jazz"]

def test_recently_searched():
    x = ['T-pain', 'SZA', 'Dreezy', 'John Legend', 'Labrinth', 'Twista', 'dvsn', 
         'Weezer', 'Flyleaf', 'Frank Ocean', 'Joji']
    assert recently_searched(x) == ['Joji', 'Frank Ocean', 'Flyleaf', 'Weezer', 'dvsn',
                                       'Twista', 'Labrinth', 'John Legend', 'Dreezy', 'SZA']
    
def test_search():
    
    #Assert statements for when the user chooses a specific artist name 
    
    artist = 'Frank Ocean'
    assert search(artist) == 7, 'R&B', 'Frank Ocean', 'Seigfried'
    assert search(artist) == 141, 'R&B', 'Frank Ocean', 'Bad Religion'
    assert search(artist) == 595, 'Alternative', 'Frank Ocean', 'Nights'
    assert search(artist) == 7, 'Alternative', 'Frank Ocean', 'Thinkin Bout You'
    assert search(artist) == 7, 'Alternative', 'Frank Ocean', 'Ivy'
    
    #Assert statements for when the user chooses a specific song 
    
    track = 'Get You Good'
    assert search(track) ==  21, 'R&B', 'Roy Woods', 'Get You Good'
    assert search(track) ==  45451, 'Hip-Hop', 'Roy Woods', 'Get You Good'
    assert search(track) ==  66345, 'pop', 'Roy Woods', 'Get You Good'
    assert search(track) ==  70207, 'Rap', 'Roy Woods', 'Get You Good'