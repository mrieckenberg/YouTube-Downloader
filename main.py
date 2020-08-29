from pytube import YouTube
from tkinter import *
import webbrowser
from tkinter import filedialog
import os

# Root
root = Tk()
root.geometry('550x150')
root.config(bg="#660066")
root.title("YouTube Downloader")


# Entries
entry1 = Entry(root,bg="#99FFCC",fg="#000033",width='50',justify='center',font=('Georgia',12,'bold'))

# Definitions
def onClick(x):
    webbrowser.open(x,new=1)

def Submit():

    iWindow = Toplevel(root)
    iWindow.geometry('800x150')
    iWindow.config(bg='#003333')
    iWindow.title("Video Information")
    global url
    url = entry1.get()
    #url = 'https://www.youtube.com/watch?v=95SYdjRVCR0'

    def search_for_file_path():
        currdir = os.getcwd()
        tempdir = filedialog.askdirectory(parent=root, initialdir=currdir, title='Please select a directory')
        if len(tempdir) > 0:
            print("You chose: %s" % tempdir)
            return tempdir

        elif len(tempdir) == 0:
            print("None chosen")
            return None

    #file_path_variable = search_for_file_path()
    #print("\nfile_path_variable = ", file_path_variable)

    def downloadVideo():
        url
        yt = YouTube(url)
        file_path_variable = search_for_file_path()
        if file_path_variable == "":
            a = "Not downloaded"
            statusLabel = Label(iWindow, text=a, bg='black', fg='red')
            statusLabel.pack()
            print(a)
        else:
            #yt = YouTube(url)
            d = yt.streams.filter(adaptive=True).first()
            #print(d)
            d.download(file_path_variable)

            if bool(d) is True:
                a = "Successful download"
                statusLabel = Label(iWindow, text=a, bg='black', fg='green')
                statusLabel.pack()
                print(a)
            else:
                print("Didn't work")

    yt = YouTube(url)
    vidTitle = Label(iWindow,bg='#003333',fg='#CCFF33',text=yt.title,font=("Georgia",17,'bold'))
    vidTitle.pack()
    vidURL = Label(iWindow,bg='#003333',fg='#33FFFF',text=url,font=("Georgia",12,"underline"))
    vidURL.pack()
    seeVid = Button(iWindow, text="See video", bg="#9999FF", fg='#000033', font=("Georgia", 12, 'bold'),command=lambda: onClick(url))
    seeVid.pack(pady=5)
    downloadButton = Button(iWindow,text="Download",font=("Georgia",10,'bold'),bg='#339900',fg='#000033',command=downloadVideo)
    downloadButton.pack()
    #seeVid = Button(iWindow,text="See video",bg="#E53F83",fg='white',font=("Georgia",12,'bold'),command=lambda: onClick(url))





# Labels
Label1 = Label(root,bg="#660066",fg="#CCFF33",text="Enter your link below",font=("Georgia",17,'bold'))

# Buttons
button1 = Button(root,bg='#3366FF',fg='#330000',text='Submit',font=("Georgia",12,'bold'),pady=10,command=Submit)

# Pack
Label1.pack(ipady=1)
entry1.pack(pady=10)
button1.pack(pady=2)







root.mainloop()
