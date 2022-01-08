import subprocess
from datetime import datetime
from math import log, floor
from os import stat, rename, remove, listdir
from os.path import getctime, isdir
from pathlib import Path
from time import time, strftime


def run_prm():
    """
    Этот сценарий используется для создания резервных копий файлов и папок, перечисленных в paths_input.
    Это делается путем создания несжатого и защищенного паролем 7-zip архива для каждого элемента в paths_input.
    Существующий архив будет перезаписан при повторном вызове скрипта. Это быстрее, чем обновление файла 7z,
    поскольку в процессе резервного копирования задействовано большое количество файлов.
    """

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    print("Перед использованием требуется дополнительная настройка скрипта.")
    exit(0)
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    # Укажите здесь входные каталоги / файлы и выходной каталог
    paths_input = [
        "D:\Backup",
        # '../folder2',
        # 'C:/folder/file1.zip'
    ]
    dir_output = 'D:/Backup'
    today = datetime.today().strftime("%Y%m%d")

    print('Для файлов резервных копий требуется пароль.')
    pw = input('Введите пароль: ')
    if not pw:
        pw = "password"  # Пароль по умолчанию

    for dir_name in paths_input:
        if isdir(dir_name):
            for file_name in listdir(dir_name):
                date_file = datetime.fromtimestamp(getctime(dir_name + "\\" + file_name)).strftime('%Y%m%d')
                if today == date_file:
                    backup(str(dir_name + "\\" + file_name), dir_output, pw)
        else:
            backup(dir_name, dir_output, pw)

    # input('Нажмите Enter, чтобы выйти...')


def backup(paths_input, dir_output, pw):
    print('Running Backup Script...\n')
    time_start_total = time()
    path_input = paths_input
    # Получить имя файла из пути ввода
    file_name = Path(path_input).stem
    if any(file_name is x for x in ('.', '..')):
        file_name = 'Backup.7z'
    else:
        # file_name = file_name + str(datetime.today().strftime("_%Y%m%d_%H%M%S")) + '.7z'
        file_name = file_name + '.7z'

    # Нормализованные пути
    path_input = str(Path(path_input))
    path_output = str(Path(dir_output) / file_name)

    # Если 7z-файл уже существует, переименовываем его в .tmp (предварительно удаляем все файлы tmp)
    path_output_tmp = path_output + '.tmp'
    if Path(path_output).is_file():
        if Path(path_output_tmp).is_file():
            print('Удаление старого временного файла:', path_output_tmp)
            remove(path_output_tmp)
        print('Создание временного файла текущей резервной копии:', path_output_tmp)
        rename(path_output, path_output_tmp)

    print('Начали:', strftime('%H:%M:%S'))
    print('Создаем:', path_input)
    time_start = time()

    # Архивируем
    success = zip(path_input, path_output, pw)

    # Если операция zip прошла успешно и файл tmp существует, удалите файл tmp
    if Path(path_output_tmp).is_file():
        if success:
            print('Успешное резервное копирование! Удаление старой резервной копии:', path_output_tmp)
            remove(path_output_tmp)
        else:
            print(
                'Временный файл старого архива все еще существует, потому что 7-zip вернул предупреждение или ошибку:',
                path_output_tmp)

    # Вывести информацию о созданном файле
    print('Создан:', path_output)
    print('Размер:', binaryprefix(stat(path_output).st_size))
    print('Время создания:', sec2hms(time() - time_start), '\n')
    print('Общее время работы:', sec2hms(time() - time_start_total), '\n')


def sec2hms(s):
    """
    Преобразует секунды в часы / минуты / секунды.
    : return: Строка в формате hms.
    """
    (h, s) = divmod(s, 3600)
    (m, s) = divmod(s, 60)
    s = round(s)
    if s == 60:
        m += 1
        if m == 60:
            h += 1
    return '{} h {} m {} s'.format(int(h), int(m), int(s))


def binaryprefix(a):
    """
    Преобразует байты в байты с двоичным префиксом. Например. 1e9 в «1 ГБ»
    : return: Строка байтов с двоичным префиксом.
    """
    units = ('B', 'kB', 'MB', 'GB', 'TB')
    b = floor(log(a, 1024))
    b = min(b, len(units))
    a = round(a / 1024 ** b, 2)
    return '{} {}'.format(a, units[b])


def zip(path_input, path_output, pw=''):
    """
    Создает контейнер 7z для path_input в path_output с паролем pw.
    : return: True, когда операция zip завершилась без предупреждений и ошибок, иначе False.
    """
    # Путь к 7-zip
    path_7z = r'C:\Program Files (x86)\7-Zip\7z.exe'
    path_7z = str(Path(path_7z))

    # Команда для сжатия
    command = [path_7z,
               'a',  # создать файл (a) dd
               path_output,
               path_input,
               # '-v50g', # создать многотомный файл размером 50 ГБ
               '-mx0',  # без сжатия
               '-p' + pw,  # Установка пароля
               '-mhe'  # зашифровать заголовки
               ]

    # print('Начали: ', subprocess.list2cmdline(command))

    # Запустить команду zip
    sp = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    # Распечатать прямой вывод из 7-zip
    everything_ok = False
    global line
    for line in sp.stdout.readlines():
        line = line.decode(encoding='utf-8', errors='ignore').rstrip()
        print('[7-zip Вывод: ]', line)

    return 'Everything is Ok' in line


if __name__ == '__main__':
    run_prm()
