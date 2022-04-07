from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
from pytube import YouTube
from idlelib.tooltip import Hovertip


def video():
    global win
    win = Tk()
    win.title("Download Video")
    win.iconbitmap("download_arrow.ico")
    win.geometry('450x250')
    win.configure(background='#ed8975')

    # -----windows widgets-----

    label = Label(win, text="Paste Video URL", font=(
        "Helvetica", 10, 'bold'), fg='#304d63')
    label.grid(row=1, column=0, padx=20, ipady=1, pady=20)

    # url entry
    global link_url
    link_url = Entry(win)
    link_url.grid(row=1, column=1, ipadx=40, ipady=3, pady=20)

    # button select folder
    btn_select = Button(win, text='⋯', command=select)
    btn_select.grid(row=1, column=4, columnspan=3, padx=10, pady=20)
    # tooltip
    tip = Hovertip(btn_select, 'Choose \nA Directory.', hover_delay=1000)

    # button download
    btn = Button(win, text="Download", width=15, command=download, height=2,
                 bg='#304d63', fg='#b2e7e8', font=('Helvetica', 10, 'bold'), bd=0)
    btn.grid(row=2, column=1, columnspan=3, padx=20)


def download():
    global link
    link = link_url.get()
    link = str(link)
    video = YouTube(link)
    video.streams.get_highest_resolution().download(
        output_path=str(folder_selected))
    video.register_on_complete_callback(finish())


def finish():
    done_msg = Label(win, text="The video was successfully downloaded!")
    done_msg.grid(row=3, column=1, pady=20)


def select():
    global folder_selected
    # set default path
    folder_selected = '/.'
    folder_selected = filedialog.askdirectory()
