print('video_title:')
from __future__ import unicode_literals
import youtube_dl

folder_name = 'converted_video_download'
audio_file_name = 'audio_file_1'

ydl_opts ={
         'outtmpl': f'/Users/eli/git_repos/python-script-extract-yt-video-data/'+folder_name+'/'+audio_file_name,
         'noplaylist': True,
         'continue_dl': True,
         'postprocessors': [{
             'key': 'FFmpegExtractAudio',
             'preferredcodec': 'wav',
             'preferredquality': '192',
             }]
     }

url ='https://www.youtube.com/watch?v=3mk2lhqGM9w'
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])



# import urllib.request
# import urllib.parse
# import re
#
# print("Please, enter search query:")
#
# query_string = urllib.parse.urlencode({"search_query" : input()})
# html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
# search_results_array = re.findall(r"watch\?v=(.{11})", html_content.read().decode())
#          #  https://www.youtube.com/watch?v=HtSuA80QTyo&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb
#
# print('Search query that provaided : %s' %(search_results_array))
# for i in search_results_array:
#    print("https://www.youtube.com/watch?v=" + i)