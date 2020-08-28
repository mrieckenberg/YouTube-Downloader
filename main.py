from pytube import YouTube
from tkinter import *
import webbrowser
from tkinter import filedialog
import os

# Root
root = Tk()
root.geometry('650x150')
root.config(bg="#3D0909")
root.title("YouTube Downloader")

#yt.streams.filter(progressive=True, subtype='mp4').order_by('resolution').desc().last().download()



# Entries
entry1 = Entry(root,bg="#DAF7A6",fg="#3D0909",width='20')


#url = 'https://www.youtube.com/watch?v=YaG5SAw1n0c'

# Definitions
def onClick(x):
    webbrowser.open(x,new=1)

def Submit():

    iWindow = Toplevel(root)
    iWindow.geometry('1000x200')
    iWindow.config(bg='black')
    global url
    url = entry1.get()

    def search_for_file_path():
        currdir = os.getcwd()
        tempdir = filedialog.askdirectory(parent=root, initialdir=currdir, title='Please select a directory')
        if len(tempdir) > 0:
            print("You chose: %s" % tempdir)

        elif len(tempdir) == 0:
            print("None chosen")
            return None

    #file_path_variable = search_for_file_path()
    #print("\nfile_path_variable = ", file_path_variable)

    def downloadVideo():
        url
        yt = YouTube(url)
        file_path_variable = ""
        file_path_variable = search_for_file_path()

        if file_path_variable == "":
            a = "Not downloaded"
            statusLabel = Label(iWindow, text=a, bg='black', fg='red')
            statusLabel.pack()
            print("Error code 3")
        else:
            d = yt.streams.filter(progressive=True, subtype='mp4').order_by('resolution').desc().last().download(file_path_variable)
            if d is None:
                a = "Not downloaded"
                statusLabel = Label(iWindow, text=a, bg='black', fg='red')
                statusLabel.pack()
                print("Error code 1")
            elif d:
                a = "Successfully downloaded"
                statusLabel = Label(iWindow, text=a, bg='black', fg='green')
                statusLabel.pack()
                print(a)
            else:
                a = "Not downloaded"
                statusLabel = Label(iWindow, text=a, bg='black', fg='red')
                statusLabel.pack()
                print("Error code 2")







    yt = YouTube(url)
    vidTitle = Label(iWindow,bg='black',fg='yellow',text=yt.title,font=("Georgia",17,'bold'))
    vidTitle.pack()
    vidURL = Label(iWindow,bg='black',fg='yellow',text=url,font=("Georgia",17,'bold'))
    vidURL.pack()
    downloadButton = Button(iWindow,text="Download",font=("Georgia",10,'bold'),bg='#09DBD3',fg='#B8024C',command=downloadVideo)
    downloadButton.pack()
    seeVid = Button(iWindow,text="See video",bg="#E53F83",fg='white',font=("Georgia",12,'bold'),command=lambda: onClick(url))
    seeVid.pack()





# Labels
Label1 = Label(root,bg="#3D0909",fg="white",text="Enter link below",font=("Georgia",17,'bold'))

# Buttons
button1 = Button(root,bg='#0BAC95',fg='#F9120B',text='Submit',pady=10,command=Submit)

# Pack
Label1.pack()
entry1.pack()
button1.pack()







root.mainloop()
