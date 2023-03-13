import tkinter as tk
from tkinter import Tk, ttk
import SpotiPy_classes as spotipy
import webview

class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.title('SpotiPy')
        self.geometry('500x500')
        self.config(bg='white')
        self.spotipy = spotipy.SpotiPy('config.json')
        self.add_song_button = ttk.Button(self, text='Add song', command=self.add_song)
        self.add_song_button.pack()
        self.find_song_button = ttk.Button(self, text='Find song', command=self.find_song)
        self.find_song_button.pack()
        self.mainloop()

    def add_song(self):
        self.destroy()
        New_Song()

    def find_song(self):
        self.destroy()
        Find_Song()



class New_Song(Tk):
    def __init__(self):
        super().__init__()
        self.title('New Song')
        self.geometry('500x500')
        self.config(bg='white')
        self.spotipy = spotipy.SpotiPy('config.json')
        self.new_song_link_label = ttk.Label(self, text='Youtube link')
        self.new_song_link_label.pack()
        self.new_song_link_entry = ttk.Entry(self)
        self.new_song_link_entry.pack()
        options = self.spotipy.get_album_list()
        self.album = tk.StringVar()
        self.album.set(options[0])
        self.new_song_album_label = ttk.Label(self, text='Album')
        self.new_song_album_label.pack()
        self.new_song_album_entry = ttk.OptionMenu(self, self.album, *options)
        self.new_song_album_entry.pack()
        self.new_song_button = ttk.Button(self, text='Add song', command=self.add_song)

        self.new_song_button.pack()
        self.return_to_main = ttk.Button(self, text='Return to main', command=self.return_to_main)
        self.return_to_main.pack()
        self.mainloop()

    def add_song(self):
        self.spotipy.add_number(
            self.album.get(),
            self.new_song_link_entry.get())

    def return_to_main(self):
        self.destroy()
        GUI()

class Find_Song(Tk):
    def __init__(self):
        super().__init__()
        self.artist_birthday = ''
        self.artist_name = ''
        self.album = ''
        self.song_title = ''
        self.title('Find Song')
        self.geometry('500x500')
        self.config(bg='white')
        self.spotipy = spotipy.SpotiPy('config.json')
        options = self.spotipy.get_number_list()
        self.song = tk.StringVar()
        self.song.set(options[0])
        self.find_song_label = ttk.Label(self, text='Song')
        self.find_song_label.pack()
        self.find_song_entry = ttk.OptionMenu(self, self.song, *options)
        self.find_song_entry.pack()
        self.find_song_button = ttk.Button(self, text='Find song', command=self.find_song)
        self.find_song_button.pack()
        self.return_to_main = ttk.Button(self, text='Return to main', command=self.return_to_main)
        self.return_to_main.pack()
        self.title_label = ttk.Label(self, text=f'Title = ')
        self.title_label.pack()
        self.length_label = ttk.Label(self, text=f'Length = ')
        self.length_label.pack()
        self.artist_name_label = ttk.Label(self, text=f'Artist = ')
        self.artist_name_label.pack()
        self.artist_birthday_label = ttk.Label(self, text=f'Birthday = ')
        self.artist_birthday_label.pack()
        self.album_label = ttk.Label(self, text=f'Album = ')
        self.album_label.pack()

        self.mainloop()

    def find_song(self):
        song = self.spotipy.find_number(self.song.get())
        self.song_title = song[1]
        artist = self.spotipy.get_artist_from_song(song[1])
        album = self.spotipy.get_album_from_song(song[1])
        self.album = album[1]
        self.artist_name = artist[1]
        self.artist_birthday = artist[2]
        link = song[3]
        length = song[2]
        self.title_label.destroy()
        self.title_label = ttk.Label(self, text=f'Title = {self.song_title}')
        self.title_label.pack()
        self.length_label.destroy()
        self.length_label = ttk.Label(self, text=f'Length = {length}')
        self.length_label.pack()
        self.artist_name_label.destroy()
        self.artist_name_label = ttk.Label(self, text=f'Artist = {self.artist_name}')
        self.artist_name_label.pack()
        self.artist_birthday_label.destroy()
        self.artist_birthday_label = ttk.Label(self, text=f"Artist's Birthday = {self.artist_birthday}")
        self.artist_birthday_label.pack()
        self.album_label.destroy()
        self.album_label = ttk.Label(self, text=f"Album = {self.album}")
        self.album_label.pack()
        webview.create_window('Song', link)
        webview.start()


    def return_to_main(self):
        self.destroy()
        GUI()





GUI()