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
                self.songs.remove(song)
                break #self.song.remove


    def total_length(self):
        playlist_total_length = 0
        for song in self.songs:
            playlist_total_length += song.length
        return playlist_total_length

    def remove_disrated(self,rating):
        result = []
        for i in range(0, len(self.songs)):
            if self.songs[i].rating >= rating:
                result.append(self.songs[i])
        self.songs = result
        return self.songs

    def remove_bad_quality(self):
        result = []
        for i in range(0, len(self.songs)):
            if self.songs[i].bitrate > Playlist.LOW_BITRATE:
                result.append(self.songs[i])
        self.songs = result
        return self.songs

    def show_artists(self):
        artists = []
        for song in self.songs:
            if song.artist not in artists:
                artists.append(song.artist)

        return artists

    def __str__(self):
        return '\n'.join("{} {} {}:{}".format(
            song.artist, song.title, song.length // 60,
            song.length % 60) for song in self.songlist)

    def save(self, file_name):
        json_dict = {"name": self.name,
                     "songs": [{"title": song.title,
                                "artist": song.artist,
                                "album": song.album,
                                "rating": song.rating,
                                "length": song.length,
                                "bitrate": song.bitrate}
                               for song in self.songs]}
        file = open(file_name, 'r+')
        file.write(json.dumps(json_dict, indent=4, separators=(',', ': ')))
        file.close()

def load(self):
    pass



