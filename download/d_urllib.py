import urllib.request

import check_out_url

url, filename = check_out_url.ch_url()


def run_prm():
    print(f'Скачиваем файл: {filename}')
    try:
        urllib.request.urlretrieve(url, filename)
    except urllib.error.HTTPError:
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv: 95.0) Gecko/20100101 Firefox/95.0'}
        req = urllib.request.Request(url=url, headers=headers)
        with open(filename, 'wb') as f:
            f.write(urllib.request.urlopen(req).read())


if __name__ == '__main__':
    run_prm()
