import json

def load(file_name):
    file = open(file_name, 'r')
    file_content = file.read()
    file_content = json.loads(content)
    file.close()
    loaded_playlist = Playlist(content['name'])
    for song in file_content['songs']:
        loaded_playlist.songs.append(
            Song(
                song['name'],
                song['artist'],
                song['album'],
                song['rating'],
                song['length'],
                song['bitrate']
            )
        )
    return loaded_playlist

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
        result = ""
        for song in self.songs:
            result += "{} {} - {}\n".format(song.artist, song.title, "{}:{}".format(int(song.length // 60), int(song.length % 60)))
        return result

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





