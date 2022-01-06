# Портфолио на junior Python
import os
import sys


def menu():
    """
    Меню запуска программ.
    Создаем список директорый с программами и выдаем его для выбора.
    :return: Список программ в выбранной директории.
    """
    example_dir = './'
    list1 = []

    # Список директорий в рабочей директории
    for i in os.listdir(example_dir):
        if os.path.isdir(i) and i not in ["venv", ".idea"]:
            list1.append(i)

    list1 = sorted(list1)
    print("Основное меню:")
    print_menu(list1)

    try:
        num = int(input("Введите номер пункта меню: "))
    except ValueError:
        print("Не правильный формат ввода. Пожалуйста укажите номер пункта")
        # Перезупуск процесса (программы)
        os.execv(sys.executable, ['python'] + [sys.argv[0]])
    else:
        if num == 0:
            exit(0)
        elif num < 0 or num > len(list1):
            print("Нет такого пункта. Пожалуйста, будьте внимательней!")
            os.execv(sys.executable, ['python'] + [sys.argv[0]])
        else:
            num_menu = num - 1
            name_dir = list1[num_menu]
            menu2(name_dir)


def menu2(name_dir=""):
    """
    Подменю запуска программ.
    :param name_dir: Имя директории с программами.
    :return: Запуск выбранной программы.
    """

    example_dir = f'./{name_dir}'
    list2 = []

    for i in os.listdir(example_dir):
        if os.path.isfile(os.path.join(example_dir, i)) \
                and i.endswith('.py'):
            list2.append(i.split(sep='.')[0])

    list2 = sorted(list2)
    print("Меню " + name_dir + ":")

    # зацикливаем меню до правильного выбора или выхода
    status = True
    while status:
        print_menu(list2)
        try:
            num = int(input("Введите номер пункта меню: "))
        except ValueError:
            print("Не правильный формат ввода. Пожалуйста укажите номер пункта")
        else:
            if num == 0:
                status = False
                os.execv(sys.executable, ['python'] + [sys.argv[0]])
            elif num < 0 or num > len(list2):
                print("Нет такого пункта. Пожалуйста, будьте внимательней!")
            else:
                status = False
                num_menu = num - 1
                name_prm = list2[num_menu]
                print("Запуск программы " + name_prm + ":", '\n')
                # Функция eval() выполняет строку-выражение
                # функция run_prm() обязательно должня быть в файлах основной
                eval(name_prm).run_prm()


def print_menu(in_list):
    """
    Создаем и распечатываем меню из массива.
    :param in_list: массив данных
    :return: выводим в консоль пронумерованный список
    """
    num = 0
    while num < len(in_list):
        for i in in_list:
            num += 1
            print(str(num) + ". " + i)
    print("0. Выход\n")


if __name__ == '__main__':
    menu()
