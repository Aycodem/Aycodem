from pytube import YouTube
from sys import argv

link=argv[1]
yt= YouTube(link)

print("title:" ,yt.title)
print("views:" ,yt.views) 


yd =yt.streams.get_highest_resolution()

yd.download("C:\Users\user\Videos\New folder")
