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