import spotipy
from spotipy.oauth2 import SpotifyOAuth

def get_playlist_tracks(playlist_id):
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='client_id_here',
                                                   client_secret='client_secret_here',
                                                   redirect_uri='redirect_url_here',
                                                   scope='playlist-read-private'))

    #please change the client_id, client_secret_key and redirect_url in the above lines

    song_names = []
    results = sp.playlist_tracks(playlist_id)

    while results:
        for item in results['items']:
            track = item['track']
            song_names.append(track['name'])

        results = sp.next(results)

    return song_names

if __name__ == "__main__":
    playlist_link = list(input("Enter the url of the playlist you want to").split("/"))
    last_playlist_id = list(playlist_link[-1].split("?"))

    songs = get_playlist_tracks(last_playlist_id[0])

    if songs:
        for index, song in enumerate(songs, 1):
            print(f"{index}. {song}")
    else:
        print("Failed to fetch playlist data.")
