import time
from tkinter import *
from tkinter import ttk
import pygame
import os
from tkinter import filedialog as fd
from mutagen.mp3 import MP3

pygame.mixer.init()

window = Tk()
window.title('Player')
window.geometry('600x400+800+300')
window.resizable(False, False)
window.config(bg='blue')
window['bg'] = '#6A5ACD'

play_img = PhotoImage(file='pictures/play.png').subsample(10)
stop_img = PhotoImage(file='pictures/stop.png').subsample(10)
next_img = PhotoImage(file='pictures/next.png').subsample(-90)
before_img = PhotoImage(file='pictures/next.png').subsample(90)
songs_names = []
directory = ''
sound = pygame.mixer.music


def import_from_direct():
    global directory
    global songs_names
    directory = fd.askdirectory()
    songs_names = os.listdir(directory)
    print(directory)
    print(songs_names)
    sound.load(directory + '/' + songs_names[0])
    songs_names_var = Variable(value=songs_names)
    listbox.config(listvariable=songs_names_var)


def select_song(event):
    index = listbox.curselection()[0]
    sound.stop()
    sound.load(directory + '/' + songs_names[index])
    start_play()


def prev_song():
    tup = listbox.curselection() + (0,)
    index = tup[0]
    listbox.select_clear(index)
    if index - 1 < 0:
        index = len(songs_names) - 1
    else:
        index -= 1
    listbox.select_set(index)
    sound.stop()
    sound.load(directory + '/' + songs_names[index])
    start_play()
    long_time['value'] = 0


def next_song():
    tup = listbox.curselection() + (0,)
    index = tup[0]
    listbox.select_clear(index)
    if index + 1 > len(songs_names) - 1:
        index = 0
    else:
        index += 1
    listbox.select_set(index)
    sound.stop()
    sound.load(directory + '/' + songs_names[index])
    start_play()
    long_time['value'] = 0


def start_play():
    tup = listbox.curselection() + (0,)
    index = tup[0]
    song = MP3(directory + '/' + songs_names[index])
    long_time['to'] = song.info.length
    if len(songs_names) > 0:
        if sound.get_pos() == -1:
            start['image'] = stop_img
            sound.play()
            return
        if start['image'] == 'pyimage4':
            start['image'] = play_img
            sound.pause()
            return
        else:
            sound.unpause()
            start['image'] = stop_img
            return
    return


def change_volume(some):
    sound.set_volume(scale.get() / 10)


def song_time(some):
    sound.set_pos(long_time.get())


start = Button(window, image=play_img, bg='#8A2BE2', fg='#FFFFFF', bd=5, command=start_play)
start.pack()

previous = Button(window, image=before_img, bg='#8A2BE2', fg='#FFFFFF', bd=5, command=prev_song)
previous.place(x=200, y=5)

next = Button(window, image=next_img, bg='#8A2BE2', fg='#FFFFFF', bd=5, command=next_song)
next.place(x=340, y=5)

select_direct = Button(window, text='Выбрать папку', bg='#8A2BE2', fg='#FFFFFF', bd=5, command=import_from_direct)
select_direct.place(x=30, y=220)

listbox = Listbox(selectmode=SINGLE, height=7, width=90, bg='#E6E6FA',
                  selectbackground='#9370DB', highlightcolor='#9370DB')
listbox.place(x=30, y=250)
listbox.bind('<<ListboxSelect>>', select_song)

scrollbar = ttk.Scrollbar(orient="vertical", command=listbox.yview)
scrollbar.place(x=15, y=250)

listbox['yscrollcommand'] = scrollbar.set

scale = ttk.Scale(orient=HORIZONTAL, length=200, from_=0, to=10.0, value=5, command=change_volume)
scale.pack()
sound.set_volume(0.5)

long_time = ttk.Scale(orient=HORIZONTAL, length=400, from_=0, command=song_time)
long_time.place(x=95, y=100)
print(sound.get_pos())

while True:
    if start['image'] == 'pyimage4':
        print(sound.get_pos())
        long_time['value'] = sound.get_pos() / 1000
    window.update()
    time.sleep(0.000001)

