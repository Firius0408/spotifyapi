import spotifywebapi as swa
import pytest
import os

@pytest.fixture
def client_setup():
    CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
    CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')
    return swa.Spotify(CLIENT_ID, CLIENT_SECRET)

@pytest.fixture
def client_get_user(client_setup: swa.Spotify):
    sp = client_setup
    return sp.getUser('ohxbrsd1nnumvgecxebefjdlo')

@pytest.fixture
def client_get_user_playlists(client_setup: swa.Spotify, client_get_user):
    sp = client_setup
    return sp.getUserPlaylists(client_get_user)

@pytest.fixture
def client_get_auth_user(client_setup: swa.Spotify):
    sp = client_setup
    REFRESH_TOKEN = os.getenv('REFRESH_TOKEN')
    return sp.getAuthUser(REFRESH_TOKEN)

def client_get_playlist_from_id(client_setup: swa.Spotify):
    sp = client_setup
    return sp.getPlaylistFromId('')

def test_client(client_setup: swa.Spotify):
    sp = client_setup
    assert sp
    with pytest.raises(swa.SpotifyError):
        swa.Spotify('notanid', 'notasecret')

def test_client_refresh(client_setup: swa.Spotify):
    sp = client_setup
    assert sp.refreshAccessToken

def test_client_get_user(client_get_user):
    user = client_get_user
    assert type(user) == type(dict())
    assert user['id'] == 'ohxbrsd1nnumvgecxebefjdlo'
    assert user['display_name'] == 'Exceptional Playlists'

def test_client_get_user_playlists(client_get_user_playlists):
    playlists = client_get_user_playlists
    assert type(playlists) == type(list(dict()))
    assert len(playlists) == 7
    assert playlists[0]['id']
    assert type(playlists[0]['tracks']) == type(dict())
    assert playlists[0]['tracks']['href']

def test_client_get_auth_user(client_get_auth_user):
    user = client_get_auth_user
    assert user
