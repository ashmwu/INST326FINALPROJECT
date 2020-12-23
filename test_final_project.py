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
