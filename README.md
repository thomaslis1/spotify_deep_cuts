# Spotify Deep Cuts

A simple Python tool that connects to the Spotify Web API and finds **an artist’s deepest cuts** — their *least popular officially released tracks*.  
Perfect for discovering hidden gems, demos, b-sides, and underrated songs.

## 📦 Requirements

```
pip install spotipy
```

---

## 🔧 Configuration

```
1. Create a Spotify App:
   https://developer.spotify.com/dashboard

2. Set:
   - CLIENT_ID
   - CLIENT_SECRET
   - REDIRECT_URI → http://127.0.0.1:8080/callback

3. Place these values inside your script or environment variables.
```

---

## ▶️ Usage

```
run python deep_cuts.py
```

```
input Artist name
input Spotify Auth URL 
```

Example output:

```
🎧 Deep cuts for Mac DeMarco:

- The Cattleman's Prayer - Demo
- Here Comes The Cowboy - Demo
- Baby Bye Bye - Demo
...
Link to Playlist
```



