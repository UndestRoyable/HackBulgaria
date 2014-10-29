import os
#from playlist import Playlist
from mutagen.easyid3 import EasyID3


class MusicCrawler:
    def __init__(self, music_directory):
        self.music_directory = music_directory

    def generate_playlist(self):
        for file in os.listdir(self.music_directory):
            if file.endswith(".mp3"):
                print(file)

crawler = MusicCrawler('/home/justtrelaxx/Music')
crawler.generate_playlist()