from tkinter import *
from PIL import ImageTk, Image

from s_video import *
from playlist import *

root = Tk()
root.title("EASY DOWNLOADER")
root.iconbitmap("download_arrow.ico")
root.geometry('450x250')

'''
color palette=b
(
	'#304d63',
	'#b2e7e8',
	'#f2d096',
	'#ed8975'
)

'''


# youtube logo

img = ImageTk.PhotoImage(Image.open('download_arrow.ico'))
label = Label(image=img, anchor='w')
label.grid(row=0, column=0, pady=20, padx=20)

# labels & entries

label_ytb = Label(root, text="EASY DOWNLOADER", font=(
    "Helvetica", 20, 'bold'), fg='#304d63', anchor='e', justify=CENTER)
label_ytb.grid(row=0, column=1, pady=20, columnspan=2)

# space labels

spc_label = Label(root)
spc_label.grid(row=2, columnspan=2)
spc_label1 = Label(root)
spc_label1.grid(row=3, columnspan=3)


# main buttonsb

btn_vd = Button(root, text='Single Video', width=15, height=2,
                bg='#ed8975', font=('Helvetica', 10, 'bold'), bd=0, command=video)
btn_vd.grid(row=4, column=1)

btn_pl = Button(root, text='Playlist', width=15, height=2,
                bg='#f2d096', font=('Helvetica', 10, 'bold'), bd=0, command=playlist)
btn_pl.grid(row=4, column=2)


root.mainloop()
