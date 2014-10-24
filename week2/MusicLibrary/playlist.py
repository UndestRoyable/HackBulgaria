import json

def sec_to_min(secs):
    m, s = divmod(secs, 60)
    h, m = divmod(m, 60)
    return "%d:%02d:%02d" % (h, m, s)

class Playlist:

    LOW_BITRATE = 128
    def __init__(self,name):
        self.name = name
        self.songs = []
        

    def add_song(self,song):
        self.songs.append(song)

    def remove_song(self,song_name):
        for song in self.songs:
            if song.title == song_name:
                self.songs.remove(song) #self.song.remove


    def total_length(self):
        playlist_total_length = 0
        for song in self.songs:
            playlist_total_length += song.length
        return playlist_total_length

    def remove_disrated(self,rating):
        for song in self.songs:
            if song.rating < rating:
                self.songs.remove(song)

    def remove_bad_quality(self):
        for song in self.songs:
            if song.bitrate <= LOW_BITRATE:
                self.songs.remove(song)

    def show_artists(self):
        artists = []
        for song in self.songs:
            if song.artist not in artists:
                artists.append(song.artist)

        return artists

    def __str__(self):
        result = ""
        for song in self.songs:
            "{} {} - {}".format(song.artist,song.title,secs_to_min(playlist.total_length()))
        pass



