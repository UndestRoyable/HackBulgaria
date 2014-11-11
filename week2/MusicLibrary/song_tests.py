import unittest
from song import Song


class SongTest (unittest.TestCase):

    def test_song_init(self):
        song = Song("Thunderstruck", "ACDC", "The Razors Edge", 5, 271.8, 320)
        self.assertEqual(song.title, "Thunderstruck")
        self.assertEqual(song.artist, "ACDC")
        self.assertEqual(song.album, "The Razors Edge")
        self.assertEqual(song.rating, 5)
        self.assertEqual(song.length, 271.8)
        self.assertEqual(song.bitrate, 320)

    def test_rate(self):
        song = Song("Thunderstruck", "ACDC", "The Razors Edge", 0, 271.8, 320)
        song.rate(5)
        self.assertEqual(song.rating, 5)

    def test_rating_out_of_range_value_error(self):
        song = Song("Thunderstruck", "ACDC", "The Razors Edge", 0, 271.8, 320)
        with self.assertRaises(ValueError):
            song.rate(8)

if __name__ == '__main__':
    unittest.main()
