import os, msvcrt, re, ctypes, pygetwindow
from tkinter.filedialog import askdirectory
from pytubefix.cli import on_progress
from pytubefix import Playlist, YouTube, helpers, innertube
from pytubefix.helpers import reset_cache
from pytubefix.exceptions import VideoUnavailable, AgeRestrictedError

# reset_cache()

token_path = os.path.join(os.getenv('APPDATA'), "YTDownloadCache", 'tokens.json')
# # , 'tokens.json'
url = "https://www.youtube.com/watch?v=l2dA6Yn62kE"

yt = YouTube(url, on_progress_callback=on_progress, use_oauth=True, allow_oauth_cache=True, token_file=token_path)
print(yt.title)

ys = yt.streams.get_highest_resolution()
ys.download()

# {"access_token": "ya29.a0Ad52N3-7E3TwSI1M8s02hMKxWzIeAp025DcvBAmvHhxdPavwguoHry4ZUiMTxEjlQbAD26dZqBdeg7MmLW9JVTuY-w84vr0OLxxCTOxBTv7hoHeq2hUBp6R1PsdM-MtaXFR2MBBheKs3NHiiv-8_rq94UH3-wSOZpk80RVOt_pvwxW7r_gaCgYKAYYSARESFQHGX2MiACe7reK5Nog7fQvxoYTOzw0185", "refresh_token": "1//09-WyEdRnSI1yCgYIARAAGAkSNwF-L9Ire2hk6lzEJatbXakrgGWsL1jpj4WN-Ry2Ekde6VZ0lIkeIOstgh_CShyl8zchhhjOYSk", "expires": 1710227673}
# {"access_token": "ya29.a0AZYkNZgJRQg5YVUXAeKmNEHlvXv1mlxXt_-Aauj4IHoPzDR__YCxKNTu74ZllAvQNsD547f5nXs93RIUUoW4lfrdFNLEIr5G6AsROnXEZ9e9XOIhKcOapdo6bHH5G711XtEq419NrDUqnqhlTx5ZMuJDdI4xa29cFpeN-9qmW4nWPzt3SOIRaCgYKARISARMSFQHGX2MiuTpM70ft_ND31b2N42d6OQ0187", "refresh_token": "1//098qY-f4Hw85hCgYIARAAGAkSNwF-L9IrqDV3dkgWqj_S99-9ZxWRP4Cm78Momgs5WdGsVJrfHNaCBcTJd4GlNjbYJYTgNBZBDAo", "expires": 1743917109, "visitorData": null, "po_token": null}

# test = '{testy}'
# print(test)
# test = test[:-1] + ', kolejne' + test[-1:]
# print(test)