import requests
import os
from PIL import Image
from pytube import YouTube


if not os.path.exists('./download'):
    os.mkdir('./download')


def getListUrls(filepath):
    # opening the file in read mode
    my_file = open(filepath, "r")
    # reading the file
    data = my_file.read()
    # replacing end splitting the text 
    # when newline ('\n') is seen.
    url_list = data.split("\n")
    my_file.close()
    return url_list

def YtDownload(links, target_dir='download/vids/'):
    if not os.path.exists(target_dir):
        os.mkdir(target_dir)

    for url in links:
        yt = YouTube(url)
        yt = yt.streams.get_highest_resolution()
        # yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        try:
            yt.download(target_dir)
        except:
            print("An error has occurred")
        print("Download is completed successfully")


def ImDownload(links, target_dir='download/imgs/'):
    if not os.path.exists(target_dir):
        os.mkdir(target_dir)

    for url in links:
        file_name = os.path.split(url)[1]
        img = Image.open(requests.get(url, stream = True).raw)
        img.save(f'{os.path.join(target_dir,file_name)}.{img.format.lower()}')
        print('Download is completed successfully')


base = 'data/'
filedata = os.path.join(base, 'urls.txt')
urls = getListUrls(filepath=filedata)

ImDownload(urls[:5])
# YtDownload(yt_urls)
print()
print('Complete')