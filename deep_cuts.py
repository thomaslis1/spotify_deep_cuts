import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# --- Spotify app config ---
CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")
REDIRECT_URI = "http://127.0.0.1:8080/callback"
SCOPE = "user-read-email"

def get_spotify_client():
    auth_manager = SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=REDIRECT_URI,
        scope=SCOPE,
        open_browser=False,
    )
    return spotipy.Spotify(auth_manager=auth_manager)

def get_artist(sp, name: str):
    res = sp.search(q=f"artist:{name}", type="artist", limit=1)
    items = res.get("artists", {}).get("items", [])
    if not items:
        print(f"No artist found for '{name}'")
        return None
    artist = items[0]
    print(f"Found artist: {artist['name']} (id={artist['id']})")
    return artist

def deep_cuts(sp, artist_name: str, n=10):
    artist = get_artist(sp, artist_name)
    if not artist:
        return
    artist_id = artist["id"]

    # Fetch albums
    albums = []
    seen = set()
    results = sp.artist_albums(
        artist_id,
        album_type="album,single,ep,compilation",
        limit=50,
    )

    while True:
        for a in results["items"]:
            if a["id"] not in seen:
                albums.append(a)
                seen.add(a["id"])
        if results["next"]:
            results = sp.next(results)
        else:
            break

    print(f"\nFound {len(albums)} albums/EPs/singles")

    # Collect tracks
    track_map = {}

    for alb in albums:
        tracks = sp.album_tracks(alb["id"], limit=50)
        for t in tracks["items"]:
            # Only include songs where this artist appears
            if any(a["id"] == artist_id for a in t["artists"]):
                track_map[t["id"]] = {
                    "name": t["name"],
                    "album": alb["name"],
                }

    print(f"Found {len(track_map)} unique track IDs that actually feature {artist['name']}")

    # Fetch popularity
    pops = {}
    track_ids = list(track_map.keys())

    for i in range(0, len(track_ids), 50):
        batch = track_ids[i:i + 50]
        resp = sp.tracks(batch)
        for tr in resp["tracks"]:
            if tr:
                pops[tr["id"]] = tr.get("popularity", 0)

    # Combine + sort
    combined = []
    for tid, info in track_map.items():
        combined.append({
            "id": tid,
            "name": info["name"],
            "album": info["album"],
            "popularity": pops.get(tid, 0)
        })

    combined.sort(key=lambda x: x["popularity"])

    # Output
    print(f"\n🎧 Deep cuts for {artist['name']}:\n")
    for t in combined[:n]:
        print(f"- {t['name']} | album: {t['album']} | popularity: {t['popularity']}")

if __name__ == "__main__":
    sp = get_spotify_client()
    artist = input("Artist name: ")
    deep_cuts(sp, artist, n=20)  # 20 deep cuts for playlist use later
