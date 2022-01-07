import requests

from download.utils import check_out_url, progressBar as pB

url, filename, content = check_out_url.ch_url()


def run_prm():
    print(f'Скачиваем файл: {filename}')
    # stream позволяет сделать получение контента по условию, а не сразу при первом запросе
    r = requests.get(url=url, stream=True)
    new_content = 0

    with open(filename, 'wb') as f:
        # используем iter_content, если stream=True
        for i in r.iter_content(chunk_size=4096):
            f.write(i)
            new_content += len(i)
            pB.updt(content, new_content)


if __name__ == '__main__':
    run_prm()
