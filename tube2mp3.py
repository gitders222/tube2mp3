import youtube_dl
import sys
import subprocess

from tkinter import *
import os
from moviepy.editor import *


global ydl_opts

ydl_opts = {
     'format': 'bestaudio/best',
     'postprocessors': [{
         'key': 'FFmpegExtractAudio',
         'preferredcodec': 'mp3',
         'preferredquality': '192',
     }],
 }


def format_number(stg):
	return stg[0] + stg[1] + ":" + stg[2] + stg[3] + ":" + stg[4] + stg[5]


def clicked():
	global ydl_opts
	global e1, e2, e3, e4
	global x1, x2, x3, x4
	x1 = e1.get()
	x2 = format_number(e2.get())
	x3 = format_number(e3.get())
	x4 = e4.get()

	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
	    result = ydl.extract_info(x1, download=False)
	    video = result['entries'][0] if 'entries' in result else result
	print(type(x4))

	url = video['url']
	path = "C:\\Users\\prettibon.WILLIE\\Documents\\div\\prosj\\tube2mp3"
	subprocess.call('ffmpeg -i "%s" -ss %s -t %s -c:v copy -c:a copy "%s"' % (url, x2, x3, x4 + ".mp4"))
	video = VideoFileClip(os.path.join(path, x4 + ".mp4"))
	video.audio.write_audiofile(os.path.join(path, x4+".mp3"))


if __name__ == "__main__":

	global e1, e2, e3, e4
	global x1, x2, x3, x4
	
	master = Tk()
	Label(master, text='URL').grid(row=0)
	Label(master, text='From (hhmmss)').grid(row=1)
	Label(master, text='Duration (hhmmss)').grid(row=2)
	Label(master, text='Name').grid(row=3)
	
	e1 = Entry(master)
	e2 = Entry(master)
	e3 = Entry(master)
	e4 = Entry(master)
	btn = Button(master, text="Update", command=clicked)
	btn.grid(column=1, row=4)
	e1.grid(row=0, column=1)
	e2.grid(row=1, column=1)
	e3.grid(row=2, column=1)
	e4.grid(row=3, column=1)
	
	master.mainloop()
