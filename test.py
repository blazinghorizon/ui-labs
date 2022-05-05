from ctypes import alignment
import os
import threading
import time
import tkinter.messagebox
from tkinter import *
from tkinter import filedialog

from tkinter import ttk
from pyparsing import col
from ttkthemes import themed_tk as tk

from mutagen.mp3 import MP3
from pygame import mixer

root = Tk()
root.title("Music Player")

mixer.init()

playlist = []

def browse_file():
    global filename_path
    filename_path = filedialog.askopenfilename()
    add_to_playlist(filename_path)

    mixer.music.queue(filename_path)

def add_to_playlist(filename):
    filename = os.path.basename(filename)
    index = 0
    playlistbox.insert(index, filename)
    playlist.insert(index, filename_path)
    index += 1

scrollbar = Scrollbar(root)
playlistbox = Listbox(root)
playlistbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=playlistbox.yview)
scrollbar.grid(row=0, rowspan=3, column=2, sticky="ns")

playlistbox.grid(row=0, column=0, rowspan=3, columnspan=2, padx=10, pady=10, sticky="news")

addBtn = ttk.Button(root, text="Add", command=browse_file)
addBtn.grid(row=3, column=0,  padx=10, sticky="ew")

def del_song():
    selected_song = playlistbox.curselection()
    selected_song = int(selected_song[0])
    playlistbox.delete(selected_song)
    playlist.pop(selected_song)

delBtn = ttk.Button(root, text="Delete", command=del_song)
delBtn.grid(row=3, column=1,  padx=10, sticky="ew")

tracknamelabel = ttk.Label(root, justify='center', text='Currently playing:\n')
tracknamelabel.grid(row=0, column=3, columnspan=5, padx=15)

sep_1 = ttk.Separator(root, orient=VERTICAL).grid(column=3, row=0, rowspan=4, sticky='wns', padx=5)

currenttimelabel = ttk.Label(root, justify='center', text='Current time: --:--/--:--')
currenttimelabel.grid(row=1, column=3, columnspan=5, padx=15)

def show_details(play_song):
    file_data = os.path.splitext(play_song)
    name = play_song.split('/')[-1][:-4]
    if len(name) > 25:
        name = name[0:24]

    tracknamelabel['text'] = 'Currently playing:\n' + name
    if file_data[1] == '.mp3':
        audio = MP3(play_song)
        total_length = audio.info.length
    else:
        a = mixer.Sound(play_song)
        total_length = a.get_length()

    mins, secs = divmod(total_length, 60)
    mins = round(mins)
    secs = round(secs)
    timeformat = '{:02d}:{:02d}'.format(mins, secs)
    currenttimelabel['text'] = currenttimelabel['text'][:-5] + timeformat

    t1 = threading.Thread(target=start_count, args=(total_length,))
    t1.start()


def start_count(t):
    global paused
    global current_time
    current_time = 0
    while current_time <= t and mixer.music.get_busy():
        if paused:
            continue
        else:
            mins, secs = divmod(current_time, 60)
            mins = round(mins)
            secs = round(secs)
            timeformat = '{:02d}:{:02d}'.format(mins, secs)
            currenttimelabel['text'] = currenttimelabel['text'][:-11] + timeformat + currenttimelabel['text'][-6:]
            time.sleep(1)
            current_time += 1


def play_music():
    global paused

    if paused:
        mixer.music.unpause()
        paused = FALSE
    else:
        try:
            stop_music()
            time.sleep(1)
            selected_song = playlistbox.curselection()
            selected_song = int(selected_song[0])
            play_it = playlist[selected_song]
            mixer.music.load(play_it)
            mixer.music.play()
            show_details(play_it)
        except:
            tkinter.messagebox.showerror('File not found', 'Melody could not find the file. Please check again.')


def stop_music():
    mixer.music.stop()

paused = FALSE

def pause_music():
    global paused
    paused = TRUE
    mixer.music.pause()


def set_vol(val):
    volume = float(val) / 100
    mixer.music.set_volume(volume)

muted = FALSE

def mute_music():
    global muted
    if muted:  # Unmute the music
        mixer.music.set_volume(0.5)
        volumeBtn.configure(image=volumePhoto)
        scale.set(50)
        muted = FALSE
    else:  # mute the music
        mixer.music.set_volume(0)
        volumeBtn.configure(image=mutePhoto)
        scale.set(0)
        muted = TRUE

n = 15

playPhoto = PhotoImage(file='images/play.png').subsample(n, n)
playBtn = ttk.Button(root, image=playPhoto, command=play_music)
playBtn.grid(row=2, column=4, padx=10)

stopPhoto = PhotoImage(file='images/stop.png').subsample(n, n)
stopBtn = ttk.Button(root, image=stopPhoto, command=stop_music)
stopBtn.grid(row=2, column=6, padx=10)

pausePhoto = PhotoImage(file='images/pause.png').subsample(n, n)
pauseBtn = ttk.Button(root, image=pausePhoto, command=pause_music)
pauseBtn.grid(row=2, column=5, padx=10)

mutePhoto = PhotoImage(file='images/mute.png').subsample(n, n)
volumePhoto = PhotoImage(file='images/volume.png').subsample(n, n)
volumeBtn = ttk.Button(root, image=volumePhoto, command=mute_music)
volumeBtn.grid(row=3, column=4)

scale = ttk.Scale(root, from_=0, to=100, orient=HORIZONTAL, command=set_vol)
scale.set(50)  # implement the default value of scale when music player starts
mixer.music.set_volume(0.5)
scale.grid(row=3, column=5, columnspan=2, pady=15, padx=20)

def on_closing():
    stop_music()
    root.destroy()

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=0)
root.grid_columnconfigure(3, weight=0)
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=0)


root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()