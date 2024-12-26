import os, msvcrt, re
from pytubefix import Playlist, YouTube, helpers, innertube
from pytubefix.exceptions import VideoUnavailable, AgeRestrictedError
from pytubefix.cli import on_progress

innertube._cache_dir = os.path.join(os.getenv('APPDATA'), "ytDownloadCache")
innertube._token_file = os.path.join(innertube._cache_dir, 'tokens.json')

download_directory = ''

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
            yt = YouTube(url, use_oauth=True, allow_oauth_cache=True)
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
                            yt = YouTube(vid_url, use_oauth=True, allow_oauth_cache=True)
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