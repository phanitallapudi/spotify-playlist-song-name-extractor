
# Spotify playlist song name extractor

This Python script allows you to fetch the names of songs from a private Spotify playlist. It utilizes the spotipy library, which provides access to the Spotify Web API, and requires authentication using the SpotifyOAuth method.


## How to use

 - Replace the placeholder values client_id_here, client_secret_here, and redirect_url_here in the script with your Spotify application credentials.
 - Run the script using Python:
 ```bash
$ python main.py
 ```
 -When prompted, enter the URL of the Spotify playlist you want to fetch the songs from.


## Output

The script will retrieve the names of songs from the specified playlist and display them on the console in the format: index. song_name.

Note: Make sure the playlist you want to fetch songs from is set to private.

Enjoy exploring your Spotify playlists!

```
$ python main.py 
  
  Enter the URL you were redirected to: <url here>

  1. 1st song
  2. 2nd song
  ....
```
## Requirements

Before running the script, make sure you have the following:
- Python 3.x
- Spotify Developer Account: Obtain the required credentials (client_id, client_secret, and redirect_uri) by creating a new Spotify application in the Spotify Developer Dashboard.
```
$ pip install spotipy
```

