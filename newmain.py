from pytube import YouTube
import os
import tkinter as tk
from tkinter import ttk
from tkinter import font, colorchooser, filedialog, messagebox

app = tk.Tk()
app.geometry('1200x800')
app.title('YouThoob Downloader')

#label making 
label1 = tk.Label(app, text='Hello User', font=('Arial', 30))
label1.pack(pady=10)

label2 = tk.Label(app, text = "Welcome to Indegenous YouTube Content Downloader", font=("arial", 24))
label2.pack(pady=40)

link = tk.StringVar()

paste_tagline = tk.Label(app, text='Paste your link here : ', font=('arial', 18))
paste_tagline.place(x=50, y=170)
pastebox = tk.Entry(app, width = 60, textvariable=link)
pastebox.place(x=350, y=174)

def download(event=None):
    x = str(link.get())
    ytvideo=YouTube(x).streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    if not os.path.exists('./youtube_videos'):
        os.mkdir('./youtube_videos')
    ytvideo .download('./youtube_videos')


#download button 
button= tk.Button(app,height=1, width=25, text='Download', bg='green', fg='white', command=download)
button.place(x=350, y=200)

app.mainloop()