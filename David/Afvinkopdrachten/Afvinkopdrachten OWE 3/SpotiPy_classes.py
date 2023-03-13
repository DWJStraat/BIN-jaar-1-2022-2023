import mysql.connector
import json
from pytube import YouTube
import datetime
import webbrowser


class SpotiPy:
    def __init__(self, config_path = 'config.json'):
        self.config = json.load(open(config_path, 'r'))
        self.db = mysql.connector.connect(
            host=self.config['host'],
            user=self.config['user'],
            password=self.config['password'],
            database=self.config['database']
        )
        self.cursor = self.db.cursor()

    def read(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def execute(self, query):
        self.cursor.execute(query)
        self.db.commit()

    def get_artist_id(self, artiest):
        query = f"SELECT artiest_id FROM artiest WHERE name = '{artiest}'"
        result = self.read(query)
        return result[0][0] if len(result) != 0 else -1

    def get_album_id(self, album):
        query = f"SELECT album_id FROM album WHERE title = '{album}'"
        result = self.read(query)
        return result[0][0] if len(result) != 0 else -1

    def add_number(self, album, youtube_link):
        length_in_seconds = YouTube(youtube_link).length
        titel = YouTube(youtube_link).title
        length = str(datetime.timedelta(seconds=length_in_seconds))
        print(length)
        album_id = self.get_album_id(album)
        query = f"INSERT INTO muzieknummers (title, duration, album_id, youtube_link) " \
                f"VALUES ('{titel}', '{length}', {album_id}, '{youtube_link}')"
        self.execute(query)

    def add_artist(self, name, birthday):
        query = f"INSERT INTO artiest (name, birthday) VALUES ('{name}', '{birthday}')"
        self.execute(query)

    def add_album(self, title, artiest):
        artiest_id = self.get_artist_id(artiest) if artiest is str() else artiest
        query = f"INSERT INTO album (title, artiest_id) VALUES ('{title}', {artiest_id})"
        self.execute(query)

    def get_number_list(self):
        query = "SELECT title FROM muzieknummers"
        numbers = self.read(query)
        for i in range(len(numbers)):
            numbers[i] = numbers[i][0]
        return numbers

    def get_album_list(self):
        query = "SELECT title FROM album"
        albums = self.read(query)
        for i in range(len(albums)):
            albums[i] = albums[i][0]
        return albums

    def number_search(self, search):
        query = f'SELECT title FROM muzieknummers WHERE title LIKE \'%{search}%\''
        numbers = self.read(query)
        for i in range(len(numbers)):
            numbers[i] = numbers[i][0]
        return numbers

    def album_info(self, album):
        query = f"SELECT title, name, birthday FROM album JOIN artiest ON album.artiest_id = " \
                f"artiest.artiest_id WHERE title = '{album}'"
        result = self.read(query)
        return result[0]

    def open_song(self, song):
        query = f'SELECT youtube_link FROM muzieknummers WHERE title = \'{song}\''
        result = self.read(query)
        result = result[0][0]
        webbrowser.open(result)

    def find_number(self, song):
        query = f'SELECT * FROM muzieknummers WHERE title = \'{song}\''
        return self.read(query)[0]

    def get_artist_from_song(self, song):
        album_id, album_name = self.get_album_from_song(song)
        artiest_id = self.read(f'SELECT artiest_id FROM album WHERE album_id = {album_id}')
        artiest_id = artiest_id[0][0]
        artiest_name = self.read(f'SELECT name FROM artiest WHERE artiest_id = {artiest_id}')
        artiest_name = artiest_name[0][0]
        artiest_birthday = self.read(f'SELECT birthday FROM artiest WHERE artiest_id = {artiest_id}')
        artiest_birthday = artiest_birthday[0][0]
        return artiest_id, artiest_name, artiest_birthday

    def get_album_from_song(self, song):
        album_id = self.read(f'SELECT album_id FROM muzieknummers WHERE title = \'{song}\'')
        album_id = album_id[0][0]
        album_name = self.read(f'SELECT title FROM album WHERE album_id = {album_id}')
        return album_id, album_name


a = SpotiPy()
print(a.get_artist_id('Rick Astley'))
b = a.get_album_list()
c = a.find_number('Never Gonna Give You Up')