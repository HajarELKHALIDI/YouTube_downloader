from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
from pytube import Playlist
from idlelib.tooltip import Hovertip


def playlist():
    wind = Tk()
    wind.title("Download Playlist")
    wind.iconbitmap("download_arrow.ico")
    wind.geometry('450x250')
    wind.configure(background='#f2d096')

    # -----windows widgets-----

    label = Label(wind, text="Paste Playlist URL", font=(
        "Helvetica", 10, 'bold'), fg='#304d63')
    label.grid(row=1, column=0, padx=20, ipady=1, pady=20)

    # url entry
    global link_url
    link_url = Entry(wind)
    link_url.grid(row=1, column=1, ipadx=40, ipady=3, pady=20)

    # button select folder
    btn_select = Button(wind, text='⋯', command=select)
    btn_select.grid(row=1, column=4, columnspan=3, padx=10, pady=20)
    # tooltip
    tip = Hovertip(btn_select, 'Choose \nA Directory.', hover_delay=1000)

    # button download
    btn = Button(wind, text="Download", width=15, command=download, height=2,
                 bg='#304d63', fg='#b2e7e8', font=('Helvetica', 10, 'bold'), bd=0)
    btn.grid(row=2, column=1, columnspan=3, padx=20)


def download():
    global link
    link = link_url.get()
    link = str(link)
    playlist = Playlist(link)
    for video in playlist.videos:
        video.streams.get_highest_resolution().download(output_path=str(folder_selected))


def select():
    global folder_selected
    # set default path
    folder_selected = '/.'
    folder_selected = filedialog.askdirectory()
