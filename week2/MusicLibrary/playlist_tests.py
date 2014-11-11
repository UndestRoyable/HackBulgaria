import unittest
from playlist import Playlist
from song import Song


class TestPlaylist (unittest.TestCase):

    def setUp(self):
        self.playlist = Playlist("TestPlaylist")
        self.song = Song("Thunderstruck", "ACDC", "The Razors Edge", 5, 271.8, 320)
        self.song2 = Song("Nothing else matters", "Metallica", "IDK", 0, 271.8, 320)
        self.playlist.add_song(self.song)
        self.playlist.add_song(self.song2)
    """def test_playlist_init(self):

        self.assertEqual(self.playlist.name, "TestPlaylist")
        self.assertListEqual(self.playlist.songs,[])"""

    def test_add_song(self):
        self.playlist.add_song(self.song)
        self.assertEqual(self.playlist.songs[0], self.song)

    def test_remove_song(self):
        self.playlist.add_song(self.song)
        song_name = "Thunderstruck"
        self.playlist.remove_song(song_name)
        self.assertNotIn(song_name, self.playlist.songs)
        #Check if removes more than 1 song if we have 3 eqqual songs!

    def test_total_length(self):
        playlist = Playlist("TestPlaylist")
        song1 = Song("Thunderstruck", "ACDC", "The Razors Edge", 5, 271.8, 320)
        song2 = Song("Thunderstruck", "ACDC", "The Razors Edge", 5, 200, 320)

        playlist.add_song(song1)
        playlist.add_song(song2)
        self.assertEqual(playlist.total_length(), 471.8)

    def test_remove_disrated(self):
        song = Song("Thunderstruck", "ACDC", "The Razors Edge", 0, 271.8, 320)
        self.playlist.add_song(song)
        self.playlist.remove_disrated(2)
        self.assertNotIn(song, self.playlist.songs)

    def test_show_artists(self):
        song1 = Song("Thunderstruck", "ACDC", "The Razors Edge", 0, 271.8, 320)
        self.playlist.add_song(song1)
        song2 = Song("Nothing else matters", "Metallica", "IDK", 0, 271.8, 320)
        self.playlist.add_song(song2)

        self.assertEqual(self.playlist.show_artists(), ["ACDC", "Metallica"])

    def test_save(self):
        playlist = Playlist("TestPlaylist")
        song1 = Song("Thunderstruck", "ACDC", "The Razors Edge", 5, 271.8, 320)
        song2 = Song("Thunderstruck", "ACDC", "The Razors Edge", 5, 200, 320)

        playlist.add_song(song1)
        playlist.add_song(song2)

        self.playlist.save("json.txt")


if __name__ == '__main__':
    unittest.main()
