import pytest
import test_final_project as fp
from builtins import side_effects
from unittest import mock

def test_createNewUser():
    m = fp.MusicApp('bob')
    user = m.createNewUser('bob')
    assert user.username == 'bob'
    
    with mock.patch("builtins.input", 
                    side_effects=["Rap", "Pop", "Jazz"]):
        assert user.fav_genres == ["Rap", "Pop", "Jazz"]
        
def test_recently_searched():
    x = ['T-pain', 'SZA', 'Dreezy', 'John Legend', 'Labrinth', 'Twista', 'dvsn', 
         'Weezer', 'Flyleaf', 'Frank Ocean', 'Joji']
    assert fp.recently_searched(x) == ['Joji', 'Frank Ocean', 'Flyleaf', 'Weezer', 'dvsn',
                                       'Twista', 'Labrinth', 'John Legend', 'Dreezy', 'SZA']
    