# File Management 
# Paste any File in the folder
# Check the Extension 
# Move the file into the desrired folder
# ex : JPEG file into the images folder..etc..


# Simple Example 
from watchdog.observers import Observer
import time 
from watchdog.events import FileSystemEventHandler
import os
import json 
import shutil

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            i = 1
            if filename != 'OTHERS':
                try:
                    extension = str(os.path.splitext(folder_to_track + '/' + filename)[1])
                    new_name = filename
                    file_exits = os.path.isfile(extension_paths[extension] + '/' + new_name)
                    while file_exits:
                        i = i + 1
                        # print(os.path.splitext(folder_to_track + '/' + new_name)[0])
                        # print(os.path.splitext(folder_to_track + '/' + new_name)[1])
                        new_name = os.path.splitext(folder_to_track + '/' + new_name)[0] + str(i) + os.path.splitext(folder_to_track + '/' + new_name)[1]
                        new_name = new_name.split("/")[4]
                        # new_name = split_name[0] + str(i) + '.' + split_name[1]
                        file_exits = os.path.isfile(extension_paths[extension] + '/' + new_name)
                    src = folder_to_track + '/' + filename
                    new_name = extension_paths[extension] + '/' + new_name 
                    os.rename(src, new_name)
                except Exception:
                    print(filename)
                
extension_paths = {
        # No name
        'noname':  '/Users/mac/Desktop/ORGANIZE/OTHERS/Others/Uncategorized',
        # audio
        '.aif':    '/Users/mac/Desktop/ORGANIZE/OTHERS/Media/Audio',
        '.cda':    '/Users/mac/Desktop/ORGANIZE/OTHERS/Media/Audio',
        '.mid':    '/Users/mac/Desktop/ORGANIZE/OTHERS/Media/Audio',
        '.midi':   '/Users/mac/Desktop/ORGANIZE/OTHERS/Media/Audio',
        '.mp3':    '/Users/mac/Desktop/ORGANIZE/OTHERS/Media/Audio',
        '.mpa':    '/Users/mac/Desktop/ORGANIZE/OTHERS/Media/Audio',
        '.ogg':    '/Users/mac/Desktop/ORGANIZE/OTHERS/Media/Audio',
        '.wav':    '/Users/mac/Desktop/ORGANIZE/OTHERS/Media/Audio',
        '.wma':    '/Users/mac/Desktop/ORGANIZE/OTHERS/Media/Audio',
        '.wpl':    '/Users/mac/Desktop/ORGANIZE/OTHERS/Media/Audio',
        '.m3u':    '/Users/mac/Desktop/ORGANIZE/OTHERS/Media/Audio',
        # text
        '.txt':    '/Users/mac/Desktop/ORGANIZE/OTHERS/Text/TextFiles/',
        '.doc':    '/Users/mac/Desktop/ORGANIZE/OTHERS/Text/Microsoft/Word',
        '.docx':   '/Users/mac/Desktop/ORGANIZE/OTHERS/Text/Microsoft/Word',
        '.odt ':   '/Users/mac/Desktop/ORGANIZE/OTHERS/Text/TextFiles/',
        '.pdf':    '/Users/mac/Desktop/ORGANIZE/OTHERS/Text/TextFiles/',
        '.rtf':    '/Users/mac/Desktop/ORGANIZE/OTHERS/Text/TextFiles/',
        '.tex':    '/Users/mac/Desktop/ORGANIZE/OTHERS/Text/TextFiles/',
        '.wks ':   '/Users/mac/Desktop/ORGANIZE/OTHERS/Text/TextFiles/',
        '.wps':    '/Users/mac/Desktop/ORGANIZE/OTHERS/Text/TextFiles/',
        '.wpd':    '/Users/mac/Desktop/ORGANIZE/OTHERS/Text/TextFiles/',
        # video
        '.3g2':    '/Users/mac/Desktop/ORGANIZE/OTHERS/Media/Video',
        '.3gp':    '/Users/mac/Desktop/ORGANIZE/OTHERS/Media/Video',
        '.avi':    '/Users/mac/Desktop/ORGANIZE/OTHERS/Media/Video',
        '.flv':    '/Users/mac/Desktop/ORGANIZE/OTHERS/Media/Video',
        '.h264':   '/Users/mac/Desktop/ORGANIZE/OTHERS/Media/Video',
        '.m4v':    '/Users/mac/Desktop/ORGANIZE/OTHERS/Media/Video',
        '.mkv':    '/Users/mac/Desktop/ORGANIZE/OTHERS/Media/Video',
        '.mov':    '/Users/mac/Desktop/ORGANIZE/OTHERS/Media/Video',
        '.mp4':    '/Users/mac/Desktop/ORGANIZE/OTHERS/Media/Video',
        '.mpg':    '/Users/mac/Desktop/ORGANIZE/OTHERS/Media/Video',
        '.mpeg':   '/Users/mac/Desktop/ORGANIZE/OTHERS/Media/Video',
        '.rm':     '/Users/mac/Desktop/ORGANIZE/OTHERS/Media/Video',
        '.swf':    '/Users/mac/Desktop/ORGANIZE/OTHERS/Media/Video',
        '.vob':    '/Users/mac/Desktop/ORGANIZE/OTHERS/Media/Video',
        '.wmv':    '/Users/mac/Desktop/ORGANIZE/OTHERS/Media/Video',
        # images
        '.ai':     '/Users/mac/Desktop/ORGANIZE/OTHERS/Media/Images',
        '.bmp':    '/Users/mac/Desktop/ORGANIZE/OTHERS/Media/Images',
        '.gif':    '/Users/mac/Desktop/ORGANIZE/OTHERS/Media/Images',
        '.jpg':    '/Users/mac/Desktop/ORGANIZE/OTHERS/Media/Images',
        '.jpeg':   '/Users/mac/Desktop/ORGANIZE/OTHERS/Media/Images',
        '.png':    '/Users/mac/Desktop/ORGANIZE/OTHERS/Media/Images',
        '.ps':     '/Users/mac/Desktop/ORGANIZE/OTHERS/Media/Images',
        '.psd':    '/Users/mac/Desktop/ORGANIZE/OTHERS/Media/Images',
        '.svg':    '/Users/mac/Desktop/ORGANIZE/OTHERS/Media/Images',
        '.tif':    '/Users/mac/Desktop/ORGANIZE/OTHERS/Media/Images',
        '.tiff':   '/Users/mac/Desktop/ORGANIZE/OTHERS/Media/Images',
        '.cr2':    '/Users/mac/Desktop/ORGANIZE/OTHERS/Media/Images',
        # internet
        '.asp':    '/Users/mac/Desktop/ORGANIZE/OTHERS/Others/Internet',
        '.aspx':   '/Users/mac/Desktop/ORGANIZE/OTHERS/Others/Internet',
        '.cer':    '/Users/mac/Desktop/ORGANIZE/OTHERS/Others/Internet',
        '.cfm':    '/Users/mac/Desktop/ORGANIZE/OTHERS/Others/Internet',
        '.cgi':    '/Users/mac/Desktop/ORGANIZE/OTHERS/Others/Internet',
        '.pl':     '/Users/mac/Desktop/ORGANIZE/OTHERS/Others/Internet',
        '.css':    '/Users/mac/Desktop/ORGANIZE/OTHERS/Others/Internet',
        '.htm':    '/Users/mac/Desktop/ORGANIZE/OTHERS/Others/Internet',
        '.js':     '/Users/mac/Desktop/ORGANIZE/OTHERS/Others/Internet',
        '.jsp':    '/Users/mac/Desktop/ORGANIZE/OTHERS/Others/Internet',
        '.part':   '/Users/mac/Desktop/ORGANIZE/OTHERS/Others/Internet',
        '.php':    '/Users/mac/Desktop/ORGANIZE/OTHERS/Others/Internet',
        '.rss':    '/Users/mac/Desktop/ORGANIZE/OTHERS/Others/Internet',
        '.xhtml':  '/Users/mac/Desktop/ORGANIZE/OTHERS/Others/Internet',
        '.html':   '/Users/mac/Desktop/ORGANIZE/OTHERS/Others/Internet',
        # compressed
        '.7z':     '/Users/mac/Desktop/ORGANIZE/OTHERS/Others/Compressed',
        '.arj':    '/Users/mac/Desktop/ORGANIZE/OTHERS/Others/Compressed',
        '.deb':    '/Users/mac/Desktop/ORGANIZE/OTHERS/Others/Compressed',
        '.pkg':    '/Users/mac/Desktop/ORGANIZE/OTHERS/Others/Compressed',
        '.rar':    '/Users/mac/Desktop/ORGANIZE/OTHERS/Others/Compressed',
        '.rpm':    '/Users/mac/Desktop/ORGANIZE/OTHERS/Others/Compressed',
        '.tar.gz': '/Users/mac/Desktop/ORGANIZE/OTHERS/Others/Compressed',
        '.z':      '/Users/mac/Desktop/ORGANIZE/OTHERS/Others/Compressed',
        '.zip':    '/Users/mac/Desktop/ORGANIZE/OTHERS/Others/Compressed',
        # disc
        '.bin':    '/Users/mac/Desktop/ORGANIZE/OTHERS/Others/Disc',
        '.dmg':    '/Users/mac/Desktop/ORGANIZE/OTHERS/Others/Disc',
        '.iso':    '/Users/mac/Desktop/ORGANIZE/OTHERS/Others/Disc',
        '.toast':  '/Users/mac/Desktop/ORGANIZE/OTHERS/Others/Disc',
        '.vcd':    '/Users/mac/Desktop/ORGANIZE/OTHERS/Others/Disc',
        # data
        '.csv':    '/Users/mac/Desktop/ORGANIZE/OTHERS/Programming/Database',
        '.dat':    '/Users/mac/Desktop/ORGANIZE/OTHERS/Programming/Database',
        '.db':     '/Users/mac/Desktop/ORGANIZE/OTHERS/Programming/Database',
        '.dbf':    '/Users/mac/Desktop/ORGANIZE/OTHERS/Programming/Database',
        '.log':    '/Users/mac/Desktop/ORGANIZE/OTHERS/Programming/Database',
        '.mdb':    '/Users/mac/Desktop/ORGANIZE/OTHERS/Programming/Database',
        '.sav':    '/Users/mac/Desktop/ORGANIZE/OTHERS/Programming/Database',
        '.sql':    '/Users/mac/Desktop/ORGANIZE/OTHERS/Programming/Database',
        '.tar':    '/Users/mac/Desktop/ORGANIZE/OTHERS/Programming/Database',
        '.xml':    '/Users/mac/Desktop/ORGANIZE/OTHERS/Programming/Database',
        '.json':   '/Users/mac/Desktop/ORGANIZE/OTHERS/Programming/Database',
        # executables
        '.apk':    '/Users/mac/Desktop/ORGANIZE/OTHERS/Others/Executables',
        '.bat':    '/Users/mac/Desktop/ORGANIZE/OTHERS/Others/Executables',
        '.com':    '/Users/mac/Desktop/ORGANIZE/OTHERS/Others/Executables',
        '.exe':    '/Users/mac/Desktop/ORGANIZE/OTHERS/Others/Executables',
        '.gadget': '/Users/mac/Desktop/ORGANIZE/OTHERS/Others/Executables',
        '.jar':    '/Users/mac/Desktop/ORGANIZE/OTHERS/Others/Executables',
        '.wsf':    '/Users/mac/Desktop/ORGANIZE/OTHERS/Others/Executables',
        # fonts
        '.fnt':    '/Users/mac/Desktop/ORGANIZE/OTHERS/Others/Fonts',
        '.fon':    '/Users/mac/Desktop/ORGANIZE/OTHERS/Others/Fonts',
        '.otf':    '/Users/mac/Desktop/ORGANIZE/OTHERS/Others/Fonts',
        '.ttf':    '/Users/mac/Desktop/ORGANIZE/OTHERS/Others/Fonts',
        # presentations
        '.key':    '/Users/mac/Desktop/ORGANIZE/OTHERS/Text/Presentation',
        '.odp':    '/Users/mac/Desktop/ORGANIZE/OTHERS/Text/Presentation',
        '.pps':    '/Users/mac/Desktop/ORGANIZE/OTHERS/Text/Presentation',
        '.ppt':    '/Users/mac/Desktop/ORGANIZE/OTHERS/Text/Presentation',
        '.pptx':   '/Users/mac/Desktop/ORGANIZE/OTHERS/Text/Presentation',
        # programming
        '.class':  '/Users/mac/Desktop/ORGANIZE/OTHERS/Programming/Java',
        '.java':   '/Users/mac/Desktop/ORGANIZE/OTHERS/Programming/Java',
        '.py':     '/Users/mac/Desktop/ORGANIZE/OTHERS/Programming/python',
        '.sh':     '/Users/mac/Desktop/ORGANIZE/OTHERS/Programming/shell',
        # spreadsheets
        '.ods':    '/Users/mac/Desktop/ORGANIZE/OTHERS/Text/Microsoft/Excel',
        '.xlr':    '/Users/mac/Desktop/ORGANIZE/OTHERS/Text/Microsoft/Excel',
        '.xls':    '/Users/mac/Desktop/ORGANIZE/OTHERS/Text/Microsoft/Excel',
        '.xlsx':   '/Users/mac/Desktop/ORGANIZE/OTHERS/Text/Microsoft/Excel',
        # system
        '.bak':    '/Users/mac/Desktop/ORGANIZE/OTHERS/Text/System',
        '.cab':    '/Users/mac/Desktop/ORGANIZE/OTHERS/Text/System',
        '.cfg':    '/Users/mac/Desktop/ORGANIZE/OTHERS/Text/System',
        '.cpl':    '/Users/mac/Desktop/ORGANIZE/OTHERS/Text/System',
        '.cur':    '/Users/mac/Desktop/ORGANIZE/OTHERS/Text/System',
        '.dll':    '/Users/mac/Desktop/ORGANIZE/OTHERS/Text/System',
        '.dmp':    '/Users/mac/Desktop/ORGANIZE/OTHERS/Text/System',
        '.drv':    '/Users/mac/Desktop/ORGANIZE/OTHERS/Text/System',
        '.icns':   '/Users/mac/Desktop/ORGANIZE/OTHERS/Text/System',
        '.ico':    '/Users/mac/Desktop/ORGANIZE/OTHERS/Text/System',
        '.ini':    '/Users/mac/Desktop/ORGANIZE/OTHERS/Text/System',
        '.lnk':    '/Users/mac/Desktop/ORGANIZE/OTHERS/Text/System',
        '.msi':    '/Users/mac/Desktop/ORGANIZE/OTHERS/Text/System',
        '.sys':    '/Users/mac/Desktop/ORGANIZE/OTHERS/Text/System',
        '.tmp':    '/Users/mac/Desktop/ORGANIZE/OTHERS/Text/System'
        }

folder_to_track = "/Users/mac/Desktop/ORGANIZE"
folder_Destination = '/Users/mac/Desktop/ORGANIZE/OTHERS'
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive = True)
observer.start()

# Exceptions

try:
    while True:
        time.sleep(5)
except KeyboardInterrupt:
    observer.stop()
observer.join()
