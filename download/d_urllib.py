import io
import shutil
import urllib.request

import check_out_url
import progressBar as pB

url, filename, content = check_out_url.ch_url()


def run_prm():
    print(f'Скачиваем файл: {filename}')

    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv: 95.0) Gecko/20100101 Firefox/95.0'}
    req = urllib.request.Request(url=url, headers=headers)

    # with open(filename, 'wb') as f:
    #     f.write(urllib.request.urlopen(req).read())

    with open(filename, 'wb') as f:
        blocksize = 131072
        fb = io.BytesIO()
        size = 0

        with urllib.request.urlopen(req) as Response:
            while True:
                buf = Response.read(blocksize)
                if not buf:
                    break
                fb.write(buf)
                size += len(buf)
                pB.updt(content, size)

        print(f'Записываем файл {filename} на диск.')
        fb.seek(0)
        shutil.copyfileobj(fb, f, length=131072)
    print("Готово.")


if __name__ == '__main__':
    run_prm()
