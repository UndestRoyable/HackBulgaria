class Song:
    MAX_RATING = 5
    MIN_RATING = 1

    def __init__(self, title, artist, album, rating, length, bitrate):
        self.title = title
        self.artist = artist
        self.album = album
        self.rating = rating
        self.length = length
        self.bitrate = bitrate

    def rate(self, user_rate):
        if user_rate >= Song.MIN_RATING and user_rate <= Song.MAX_RATING:
            self.rating = user_rate
        else:
            raise ValueError("Invalid rating! The rating must be between 0..5!")

    def __repr__(self):
        return str(self.__dict__)
