# Needs id3reader: http://nedbatchelder.com/code/modules/id3reader.py
#
# TODO: command-line arguments:

import os, re, id3reader

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

        filename = re.sub('[\\/:\*\?"<>\|]', '', artist + album + track + title + '.mp3')

        print file, ' -> ', filename	#print filename
        os.rename(file, filename)
