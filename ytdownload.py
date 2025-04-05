import os, msvcrt, re, ctypes, pygetwindow
from tkinter.filedialog import askdirectory
from pytubefix.cli import on_progress
from pytubefix import Playlist, YouTube, helpers, innertube
from pytubefix.exceptions import VideoUnavailable, AgeRestrictedError
# Font and size stuff
LF_FACESIZE = 32
STD_OUTPUT_HANDLE = -11

class COORD(ctypes.Structure):
    _fields_ = [("X", ctypes.c_short), ("Y", ctypes.c_short)]

class CONSOLE_FONT_INFOEX(ctypes.Structure):
    _fields_ = [("cbSize", ctypes.c_ulong),
                ("nFont", ctypes.c_ulong),
                ("dwFontSize", COORD),
                ("FontFamily", ctypes.c_uint),
                ("FontWeight", ctypes.c_uint),
                ("FaceName", ctypes.c_wchar * LF_FACESIZE)]

font = CONSOLE_FONT_INFOEX()
font.cbSize = ctypes.sizeof(CONSOLE_FONT_INFOEX)
font.nFont = 12
font.dwFontSize.X = 11
font.dwFontSize.Y = 32
font.FontFamily = 54
font.FontWeight = 700
font.FaceName = "Liberation Mono"

handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
ctypes.windll.kernel32.SetCurrentConsoleFontEx(
        handle, ctypes.c_long(False), ctypes.pointer(font))
os.system("title YTDownload")
window = pygetwindow.getWindowsWithTitle('YTDownload')[0]
window.size = (1280, 360)
# ---


# Managing dir's
# Old workaround for changing cache directory
# innertube._cache_dir = os.path.join(os.getenv('APPDATA'), "YTDownloadCache")
# innertube._token_file = os.path.join(innertube._cache_dir, 'tokens.json')

cache_dir = os.path.join(os.getenv('APPDATA'), "YTDownloadCache")
token_directory = os.path.join(cache_dir, 'tokens.json')

if not os.path.exists(cache_dir):
    os.makedirs(cache_dir)

settingsdirectory = os.path.join(cache_dir, 'settings.txt')

if os.path.isfile(settingsdirectory):
    directory = open(settingsdirectory, "r")
    download_directory = directory.read()
else:
    directory = open(settingsdirectory, "x")
    download_directory = ''
directory.close()

# Update token to work with new YT API HTTP requests
# Only updates whether user has old token file which does not contain visitorData and po_token fields
if os.path.isfile(token_directory):
    token_file = open(token_directory)
    token_string = token_file.readline()
    if 'visitorData' not in token_string:
        token_file = open(token_directory, '+w')
        token_string = token_string[:-1] + ', "visitorData": null' + token_string[-1:]
        token_file.write(token_string)
    if 'po_token' not in token_string:
        token_file = open(token_directory, '+w')
        token_string = token_string[:-1] + ', "po_token": null' + token_string[-1:]
        token_file.write(token_string)
    token_file.close()
# ---


def cls():
    return os.system('cls')


def tryagain(function, argument):
    while True:
            cls()
            print('Something went wrong')
            menu = input('Would you like to try again?(Y/n):')
            if menu == 'Y' or menu == 'y':
                function(argument)
                break
            elif menu == 'N' or menu == 'n':
                break
            else:
                continue

def download(va, yt):
    if va == 'video':
        print('Started downloading "%s"' % yt.title)
        try:
            yt.streams.get_highest_resolution().download(output_path=download_directory)
            print()
        except AgeRestrictedError:
            print('Video "%s" is age restricted' % yt.title)
        except VideoUnavailable:
            print('Video "%s" is not available' % yt.title)
    elif va == 'audio':
        print('Started downloading "%s" audio only' % yt.title)
        # title = re.sub(r'[\\/:*?"<>|]', '', yt.title)
        title = helpers.safe_filename(yt.title)
        try:
            yt.streams.get_audio_only().download(output_path=download_directory, filename=title+' audio.m4a')
            print()
        except AgeRestrictedError:
            print(AgeRestrictedError)
        except VideoUnavailable:
            print(VideoUnavailable)


def ytDownload(va):
    cls()
    try:
        url = input('Please insert the url:')
    except:
        tryagain(ytDownload, va)
    else:
        try:
            yt = YouTube(url, use_oauth=True, allow_oauth_cache=True, on_progress_callback=on_progress, token_file=token_directory)
        except:
            tryagain(ytDownload, va)
        else:
            download(va, yt)
            print('Download finished', end='')
            input()


def playlistDownload(va):
    cls()
    try:
        url = input('Please insert the url:')
    except:
        tryagain(playlistDownload, va)
    else:
        check = re.search('list=', url)
        if check:
            try:
                pl = Playlist(url)
            except:
                tryagain(playlistDownload, va)
            else:
                try:
                    for vid_url in pl.video_urls:
                        try:
                            yt = YouTube(vid_url, use_oauth=True, allow_oauth_cache=True, token_file=token_directory)
                        except:
                            print('Something went wrong')
                        else:
                            download(va, yt)
                    print('Download finished', end='')
                    input()
                except:
                    tryagain(playlistDownload, va)
        else:
            tryagain(playlistDownload, va)


def youtubeMenu(arg):
    while True:
        cls()
        print('[1] Video')
        print('[2] Audio Only')
        print('[3] Back')
        try:
            menu = int(msvcrt.getch())
        except:
            continue
        if menu == 1:
            if arg == 1:
                ytDownload('video')
            elif arg == 2:
                playlistDownload('video')
            break
        elif menu == 2:
            if arg == 1:
                ytDownload('audio')
            elif arg == 2:
                playlistDownload('audio')
            break
        elif menu == 3:
            break
        else:
            continue


def dir():
    while True:
        cls()
        print('Please select new download directory(close window to reset dir):')
        dir = askdirectory(title='Select Folder')
        if dir != '' and os.path.isdir(dir):
            directory = open(settingsdirectory, "w")
            directory.write(dir)
            directory.close()
            globals()['download_directory'] = dir
            break
        else:
            directory = open(settingsdirectory, "w")
            directory.write('')
            directory.close()
            globals()['download_directory'] = ''
            break


def main():
    while True:
        cls()
        print('[1] Youtube Video')
        print('[2] Youtube Playlist')
        if download_directory == '':
            print('[3] Change Download directory (Current: Where the exe is)')
        else:
            print('[3] Change Download directory (Current: "%s")' % download_directory)
        print('[4] Exit')
        try:
            menu = int(msvcrt.getch())
        except:
            continue
        if menu == 1:
            youtubeMenu(1)
            continue
        elif menu == 2:
            youtubeMenu(2)
            continue
        elif menu == 3:
            dir()
            continue
        elif menu == 4:
            break
        else:
            continue
main()