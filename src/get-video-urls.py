import datetime

from pytube import Playlist, YouTube

def get_data(playlist): 
    for url in playlist.video_urls:
        yt = YouTube(url)
        try:
            string = "- [ ] [{}]({}) {}\n"
            f.write(string.format(str(datetime.timedelta(seconds=round(yt.length))), url, yt.title))
        except:
            string = "- [ ] [TODO]({})\n"
            f.write(string.format(url, url))

playlists = [
    Playlist(
        'https: // www.youtube.com/playlist?list=PLlrxD0HtieHhS8VzuMCfQD4uJ9yne1mE6'),
    Playlist(
        'https://www.youtube.com/playlist?list=PLlrxD0HtieHiXd-nEby-TMCoUNwhbLUnj'),
]

f = open("playlist-details.md", "a")

for playlist in playlists:
    get_data(playlist)

f.close()
