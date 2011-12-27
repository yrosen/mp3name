##
# mp3name - names a directory full of MP3 files according to their ID3 tag data.
# I like my files as "Artist - Album - Track - Title.mp3"
#
# By Yudi Rosen (yudi42@gmail.com)
##

import os, re

try:
	import id3reader
except:
	print "Error: mp3name requires id3reader (http://nedbatchelder.com/code/modules/id3reader.py)"
	sys.exit(1)

def main():
	# Start crawling the current directory:
	for file in os.listdir('.' + os.sep):
		ext = os.path.splitext(file)

		if ext[1] == '.mp3':
			# Construct a reader from a file or filename.
			id3r = id3reader.Reader(file)

			#Artist, album, title:
			artist = id3r.getValue('performer') + ' - ' if(len(id3r.getValue('performer')) != 0) else ''
			album  = id3r.getValue('album')     + ' - ' if(len(id3r.getValue('album'))     != 0) else ''
			title  = id3r.getValue('title')             if(len(id3r.getValue('title'))     != 0) else ext[0]

			# Sometimes track is stored like 06/10, we just want the 06:
			track = re.sub('/\d+', '', id3r.getValue('track'))

			# TODO: Somehow get max len() of track? (e.g. 01 vs 001)
			if len(track) == 0:
				track = ''
			elif len(track) == 1:
				track = '0' + track + ' - '
			elif len(track) == 2:
				track = track + ' - '

			# Get rid of bad characters:
			filename = re.sub('[\\/:\*\?"<>\|]', '', artist + album + track + title + '.mp3')

			print file, ' -> ', filename
			os.rename(file, filename)

		
if __name__ == "__main__":
        main()
