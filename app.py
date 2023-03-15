from pytube import YouTube

yt = YouTube("https://youtu.be/bwzL5PMSkEc")

file = yt.streams.get_highest_resolution()

file.download()