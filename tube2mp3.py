#import youtube_dl
import yt_dlp
from yt_dlp.utils import download_range_func
import sys
import subprocess

from tkinter import *
import os
from moviepy.editor import *

PATH = "C:\\Users\\ato\\Documents\\tube2mp3-main\\videos"




###global ydl_opts

#ydl_opts = {
 #    'format': 'bestaudio/best',
 #    'postprocessors': [{
 #        'key': 'FFmpegExtractAudio',
 #        'preferredcodec': 'mp3',
 #        'preferredquality': '192',
 #    }],
 #}


def format_number(stg):
	#temp = stg[0] + stg[1] + ":" + stg[2] + stg[3] + ":" + stg[4] + stg[5]
	n_str = ["","",""]
	n = [0,0,0]
	n_str[0] = stg[0] + stg[1]
	n_str[1] = stg[2] + stg[3]
	n_str[2] = stg[4] + stg[5]

	n[0] = int(n_str[0])*60*60
	n[1] = int(n_str[1])*60
	n[2] = int(n_str[2])

	temp = n[0] + n[1] + n[2]


	return temp

def clicked():
	global ydl_opts
	global e1, e2, e3, e4
	global x1, x2, x3, x4
	x1 = e1.get()
	x2 = format_number(e2.get())
	x3 = format_number(e3.get())
	x4 = e4.get()
	print(x2)
	print(x3)

	yt_opts = {
		'verbose': True,
		'download_ranges': download_range_func(None, [(x2, x3)]),
		'force_keyframes_at_cuts': True,
	}

	with yt_dlp.YoutubeDL(yt_opts) as ydl:
		ydl.download(x1)


	#with youtube_dl.YoutubeDL(ydl_opts) as ydl:
	#	result = ydl.extract_info(x1, download=False)
	#	video = result['entries'][0] if 'entries' in result else result
	#	print(type(x4))
	#	url = video['url']
	#	path = PATH
	#	subprocess.call('ffmpeg -i "%s" -ss %s -t %s -c:v copy -c:a copy "%s"' % (url, x2, x3, x4 + ".mp4"))
	#	if check_var:
	#		print("Video")
	#		video = VideoFileClip(os.path.join(path, x4 + ".mp4"))
	#	else:
	#		print("Audio only")
	#		video = VideoFileClip(os.path.join(path, x4 + ".mp4"))
	#		video.audio.write_audiofile(os.path.join(path, x4+".mp3"))


if __name__ == "__main__":

	global e1, e2, e3, e4, check_var
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
	check_var = BooleanVar()
	checkbutton = Checkbutton(master, text="Video", variable=check_var)
	#btn = Button(master, text="Update", command=clicked)
	#btn.grid(column=1, row=4)
	e1.grid(row=0, column=1)
	e2.grid(row=1, column=1)
	e3.grid(row=2, column=1)
	e4.grid(row=3, column=1)
	

	
	checkbutton.grid(row=4, column=0)
	btn = Button(master, text="Update", command=clicked)
	btn.grid(column=1, row=4)

	master.mainloop()
