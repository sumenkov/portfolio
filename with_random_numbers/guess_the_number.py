from random import randint


def computer_number(min_num, max_num):
    """
    Функция, которая генерирует случайное число на основе диапазона, переданного в качестве аргументов.
    возвращает случайное целое число
    """
    return randint(min_num, max_num)


def player_guess(min_num, max_num):
    """
    Функция, которая запрашивает у игрока число.
    возвращает случайное целое число
    """
    user_input = int(input(f'Угадай число от {min_num} до {max_num}: '))
    return user_input


def run_prm():
    # определить верхний и нижний диапазон числа
    low = 0
    high = 10

    # получаем число от компьютера и игрока
    computer_choice = computer_number(low, high)
    player_choice = player_guess(low, high)

    # цикл, пока игрок не угадает число
    while player_choice != computer_choice:
        if player_choice > computer_choice:
            player_choice = int(input('Число слишком велико, попробуйте еще раз: '))
        elif player_choice < computer_choice:
            player_choice = int(input('Число слишком мало, попробуйте еще раз: '))

    print(f'Поздравляю! Вам удалось угадать число {computer_choice}')


if __name__ == '__main__':
    run_prm()
