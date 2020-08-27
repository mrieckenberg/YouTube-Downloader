from pytube import YouTube

path = r"C:\Users\matth\OneDrive\Desktop"

link = open('links.txt','r')

for i in link:
    yt = YouTube(1)
    vids = yt.streams.filter(progressive=True).first()
    vids.download(path)

print("Success")