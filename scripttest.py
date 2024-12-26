from pytube import Playlist, YouTube
from pytube.exceptions import VideoUnavailable

playlist_url = input('Wprowadź url playlisty: ')
# playlist_url = 'https://www.youtube.com/watch?v=E68N5E1d0_M&list=PLTeUd_6deLgE9en5_7t3AzergVdtrdnEI&pp=gAQBiAQB'
# playlist_url = 'https://www.youtube.com/playlist?list=PLhtWp_HFhsyKKAv3IDQuNpMGYlisZpOKJ'

dest = input('Wprowadź miejsce docelowe: ')

p = Playlist(playlist_url)

for url in p.video_urls:
    try:
        yt = YouTube(url)
    except VideoUnavailable:
        print('Film "%s" jest niedostępny.' % yt.title)
    else:
        print('Pobieranie "%s"' % yt.title)
        yt.streams.get_audio_only().download(dest)