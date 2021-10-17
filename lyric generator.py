# Title: Create a GUI to extract lyrics from a song Using Python
#  Author: kumar_satyam
#  Date: 29 Dec, 2020
#  Code version: Python3
#  Availability: https://www.geeksforgeeks.org
# ----------------------------------------------
# (Version Python3)[Source code].https://www.geeksforgeeks.org
#--------------------------------------------------------------


#Import necessary modules
from tkinter import *
from lyrics_extractor import SongLyrics

def get_lyrics():
    lyrics = SongLyrics("AIzaSyDqRPlCYyUv4pfmdP5iCy1XKPuGy7lpk4s","097cf1964a18a3827")

    temp = lyrics.get_lyrics(str(song_entry.get()))
    res = temp['lyrics']
    result.set(res)

#Object of tkinter
t = Tk()
t.config(bg="#900C3F")
t.title("Lyric Generator")


#Variable class in tkinter
result = StringVar()

#  Labels - Song Entry, Result
Label(t, text="Enter Song", font= "Arial",bg ="#900C3F").grid(row=0, sticky=W)
Label(t, text="Result", font = "Arial",bg="#900C3F").grid(row=3, sticky=W)

# Label for class varibale
# name using entry widget
Label(t, text="", font = "Arial",textvariable=result, bg = "#900C3F").grid(row=3, column=1, sticky=W)

song_entry = Entry(t, width=50)
song_entry.grid(row=0, column=1)

# Create search lyric button
btn = Button(t, text="Search", command=get_lyrics, bg="white")
btn.grid(row=0, column=2, columnspan=2, rowspan=2, padx=5, pady=5,)

#Execute
mainloop()
