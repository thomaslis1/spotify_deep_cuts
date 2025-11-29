# Deep Cuts – Spotify Script

A simple Python tool that connects to the Spotify Web API and finds **an artist’s deepest cuts** — their *least popular officially released tracks*.  
Perfect for discovering hidden gems, demos, b-sides, and underrated songs.

---

## ⭐ Features

```
- Authenticate with Spotify (OAuth)
- Search any artist
- Fetch all albums/EPs/singles they actually appear on
- Gather all track popularity scores
- Merge duplicate releases into single “distinct” songs
- Return the least-popular 10–20 tracks
- Playlist creation support coming next
```

---

## 🚀 How it Works

```
1. Authenticate with Spotify.
2. Search for the chosen artist.
3. Collect all their albums, EPs, singles, and compilations.
4. Gather all track IDs where the artist is actually credited.
5. Merge duplicate versions (album/single/demo).
6. Sort by Spotify’s popularity metric (0–100).
7. The lowest-popularity tracks = the deep cuts.
```

---

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
python deep_cuts.py
```

```
Artist name: mac demarco
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

---

## 🎶 Next Steps

```
- Auto-generate a Spotify playlist of deep cuts
- Web UI
- Deployable online tool
```


