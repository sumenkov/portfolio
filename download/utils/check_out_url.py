import urllib.request


def ch_url():
    # https://www.fonstola.ru/download.php?file=201111/1680x1050/fonstola.ru-60644.jpg
    # http://speedtest.ftp.otenet.gr/files/test10Mb.db
    # http://speedtest.ftp.otenet.gr/files/test100Mb.db
    url = input("Пожалуйста вставьте или напишите ссылку на файл:\n")

    try:
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv: 95.0) Gecko/20100101 Firefox/95.0'}
        req = urllib.request.Request(url=url, headers=headers)
        response = urllib.request.urlopen(req)
        # размер файла
        content_length = int(response.headers.get('Content-Length', 0))
        # достаем имя файла, если не указано, берем из ссылки
        file_name = response.headers.get('Content-Disposition',
                                         '"' + url.split('/')[-1])  # для второго split добавили в начало имени "
        file_name = file_name.split(';')[-1]
        file_name = file_name.split('"')[1]
    except ValueError:
        print("Что-то не так с ссылкой. Попробуйте указать полный адрес.")
        exit()
    else:
        return url, file_name, content_length
