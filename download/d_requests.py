import requests

import check_out_url

url, filename = check_out_url.ch_url()


def run_prm():
    print(f'Скачиваем файл: {filename}')
    r = requests.get(url=url)
    with open(filename, 'wb') as f:
        f.write(r.content)


if __name__ == '__main__':
    run_prm()
