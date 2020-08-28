from pytube import YouTube
from tkinter import *

# Root
root = Tk()
root.geometry('650x150')
root.config(bg="#3D0909")
root.title("YouTube Downloader")

# yt.streams.filter(progressive=True, subtype='mp4').order_by('resolution').desc().last().download()

# Get url
#url = entry1.get()
#print(url)
#url = input("Enter link: ")

# Entries
entry1 = Entry(root,bg="#DAF7A6",fg="#3D0909",width='20')

# Definitions
def downloadVideo():
    pass


def Submit():
    iWindow = Toplevel(root)
    iWindow.geometry('1000x100')
    iWindow.config(bg='black')
    url = 'https://www.youtube.com/watch?v=gQrkvZeE3Uc'
    yt = YouTube(url)
    vidTitle = Label(iWindow,bg='black',fg='yellow',text=yt.title,font=("Georgia",17,'bold'))
    vidTitle.pack()
    vidURL = Label(iWindow,bg='black',fg='yellow',text=url,font=("Georgia",17,'bold'))
    vidURL.pack()
    downloadButton = Button(iWindow,text="Download",font=("Georgia",10,'bold'),bg='#09DBD3',fg='#B8024C')
    downloadButton.pack()









# Labels
Label1 = Label(root,bg="#3D0909",fg="white",text="Enter link below",font=("Georgia",17,'bold'))

# Buttons
button1 = Button(root,bg='#0BAC95',fg='#F9120B',text='Submit',pady=10,command=Submit)

# Pack
Label1.pack()
entry1.pack()
button1.pack()







root.mainloop()
