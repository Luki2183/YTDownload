import os, msvcrt, re
from pytubefix import YouTube, innertube
from pytubefix.exceptions import VideoUnavailable, AgeRestrictedError

innertube._cache_dir = os.path.join(os.getenv('APPDATA'), "ytDownloadCache")
innertube._token_file = os.path.join(innertube._cache_dir, 'tokens.json')

download_directory = ''
probl = 'Something went wrong'

def cls():
    return os.system('cls')
# url1 = "https://www.youtube.com/watch?v=qnC82S70H6I"

# yt = YouTube(url1, use_oauth=True, allow_oauth_cache=True)
# ys = yt.streams.get_highest_resolution()
# ys.download()



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
                pldownload('video')
            break
        elif menu == 2:
            if arg == 1:
                ytDownload('audio')
            elif arg == 2:
                pldownload('audio')
            break
        elif menu == 3:
            break
        else:
            continue


def dir():
    while True:
        cls()
        dir = input('Please input download directory(press enter to reset dir):')
        if dir != '':
            globals()['download_directory'] = dir
            break
        else:
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