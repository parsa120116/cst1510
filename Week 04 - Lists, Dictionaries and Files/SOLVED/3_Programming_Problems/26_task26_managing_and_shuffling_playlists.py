import random

playlist = ["Song A", "Song B", "Song C", "Song D"]


def show_playlist(songs):
    """Print the playlist with position numbers."""
    for position, song in enumerate(songs, start=1):
        print(f"  {position}. {song}")


def add_song(songs, title):
    """Add a song to the end of the playlist."""
    songs.append(title)
    print(f"Added: {title}")


def remove_song(songs, title):
    """Remove a song if it is in the playlist."""
    if title in songs:
        songs.remove(title)
        print(f"Removed: {title}")
    else:
        print(f"'{title}' is not in the playlist.")


def shuffle_playlist(songs):
    """Shuffle the playlist in place."""
    random.shuffle(songs)
    print("Playlist shuffled!")


print("Starting playlist:")
show_playlist(playlist)

add_song(playlist, "Song E")
remove_song(playlist, "Song B")
remove_song(playlist, "Song Z")
print("Playlist now:")
show_playlist(playlist)

answer = input("Shuffle the playlist? (y/n): ").strip().lower()
while answer == "y":
    shuffle_playlist(playlist)
    show_playlist(playlist)
    answer = input("Shuffle again? (y/n): ").strip().lower()

print("Enjoy your music!")
