"""
This script removes a substring from a filename.
BackStory: I downloaded bunch of mp3 files from webmusic.in and
as expected all of them had "_(webmusic.in)" sub string attached to them.
And as such I put on my geeky hat and wrote this simple script to
remove the substring in the file.
"""

import os

for filename in os.listdir('.'):
	if filename.startswith("(webmusic.in)_"):
		os.rename(filename, filename[14:])
	elif (filename.find("_(webmusic.in)")!= -1):
		index = filename.find("_(webmusic.in)")
		end_index = filename.find(".mp3")
		new_filename = filename[:index] + filename[end_index:]
		os.rename(filename, new_filename)

