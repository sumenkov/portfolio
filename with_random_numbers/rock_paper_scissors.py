from random import randint


def user_interface(options):
    """
    Функция, показывающая варианты и запрашивающая отзывы игроков
    возвращает целое число.
    """
    status = True
    while status:
        for index, option in enumerate(options):
            print(f'{int(index) + 1}. {option}')

        try:
            user_input = int(input('Что вы выбираете? (напишите номер) '))
        except ValueError:
            print("Нет такого пункта. Пожалуйста, будьте внимательней!\n")
        else:
            if user_input in [1, 2, 3]:
                status = False
                return user_input - 1
            else:
                print("Нет такого пункта. Пожалуйста, будьте внимательней!\n")


def computer_choice(content):
    """
    функция, которая генерирует случайное число на основе доступных опций.
    возвращает случайное целое число
    """
    computer_chose = randint(0, len(content) - 1)
    return computer_chose


def check_results(choices, player, computer):
    """
    функция, которая проверяет, кто выиграл.
    возвращает строку
    """
    if player == computer:
        return 'Ничья.'
    elif (player == 0 and computer == len(choices) - 1) or (
            player > computer and not (player == len(choices) - 1 and computer == 0)):
        return 'Игрок проиграл.'
    return 'Игрок выиграл!'


def play():
    print(''' Добро пожаловать в «Камень, ножницы, бумага».\n Пожалуйста, выберите свое оружие.\n''')

    # определяем варианты и попросим игрока выбрать один
    options_list = ['Камень', 'Ножницы', 'Бумага']
    player_result = user_interface(options_list)
    computer_result = computer_choice(options_list)

    # визуальное представление в терминале, чтобы мы могли видеть, что выбирали обе стороны
    print(f'    Игрок выбрал: {options_list[player_result]}')
    print(f'Компьютер выбрал: {options_list[computer_result]}')

    # Проверяем результат и показываем победителя
    results = check_results(options_list, player_result, computer_result)
    print(f'\n{results}')


def run_prm():
    # Предлагаем поиграть еще раз
    play_again = ''
    while play_again.lower() not in ['n', 'N', 'т', 'Т']:
        play()
        print(f'Ты хочешь снова сыграть? ')
        play_again = input("введите N если нет (поумолчанию игра продолжается): ")


if __name__ == '__main__':
    run_prm()
