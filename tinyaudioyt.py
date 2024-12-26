import os, re, msvcrt
from pytube import YouTube, Playlist, helpers, innertube
from pytube.exceptions import VideoUnavailable, AgeRestrictedError


innertube._cache_dir = os.path.join(os.getenv('APPDATA'), "YTDownloadCache")
innertube._token_file = os.path.join(innertube._cache_dir, 'tokens.json')


def cls():
    return os.system('cls')


def tryagain():
    cls()
    print('Something went wrong, please try again')
    input()


def check(url):
    if re.search('list=', url):
        return True
    else:
        return False


def downl(yt):
    print('Downloading "%s"' % yt.title)
    try:
        yt.streams.get_audio_only().download()
    except AgeRestrictedError:
        print(AgeRestrictedError)
    except VideoUnavailable:
        print(VideoUnavailable)


def check_downl(url):
    cls()
    if check(url):
        try:
            pl = Playlist(url)
        except:
            tryagain()
        else:
            try:
                print('Started downloading playlist')
                for vid_url in pl.video_urls:
                    try:
                        yt = YouTube(vid_url, use_oauth=True, allow_oauth_cache=True)
                    except:
                        tryagain()
                    else:
                        downl(yt)
                print('Download finished', end='')
                input()
            except:
                tryagain()
    else:
        try:
            yt = YouTube(url, use_oauth=True, allow_oauth_cache=True)
        except:
            tryagain()
        else:
            downl(yt)
            print('Download finished', end='')
            input()


def main():
    while True:
        cls()
        try:
            url = input('Please input url:\n')
        except:
            tryagain()
        else:
            if url == 'exit':
                cls()
                break
            # temporary^
            try:
                if check(url):
                    pl = Playlist(url)
                else:
                    yt = YouTube(url)
            except:
                tryagain()
            else:
                check_downl(url)
main()