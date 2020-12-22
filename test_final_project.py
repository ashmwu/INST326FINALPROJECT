import pytest
import final_project as fp

def test_recently_searched():
    x = ['T-pain', 'SZA', 'Dreezy', 'John Legend', 'Labrinth', 'Twista', 'dvsn', 
         'Weezer', 'Flyleaf', 'Frank Ocean', 'Joji']
    assert fp.recently_searched(x) == ['Joji', 'Frank Ocean', 'Flyleaf', 'Weezer', 'dvsn',
                                       'Twista', 'Labrinth', 'John Legend', 'Dreezy', 'SZA']
    
def test_createNewUser():
    m = fp.MusicApp('bob')
    #with mock
    user = m.createNewUser('bob')
    assert user.username == 'bob'
    assert user.fav_genres == []