def ch_url():
    # url = 'https://www.fonstola.ru/download.php?file=201111/1680x1050/fonstola.ru-60644.jpg'
    url = input("Пожалуйста вставьте или напишите ссылку на файл:\n")
    filename = url.split('/')[-1]

    return url, filename