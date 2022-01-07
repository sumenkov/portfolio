from pytube import YouTube
from pytube.exceptions import VideoUnavailable

from download.utils import check_out_url


def run_prm():
    url, _, _ = check_out_url.ch_url()
    # url = https://www.youtube.com/watch?v=NyN23EVyXYA
    try:
        yt = YouTube(url)
    except VideoUnavailable:
        print(f'Видео {url} недоступно, пропускаю.')
    else:
        print(f'Загрузка видео : {url}')
        try:
            yt.streams.get_highest_resolution().download()
        except VideoUnavailable:
            print(f'Это видео {url} больше не доступно, пропускаю.')
    print("Закончили.")


if __name__ == '__main__':
    run_prm()
