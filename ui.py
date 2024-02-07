from logger import input_data, print_data

def interface():
    print('Добрый день! Я бот-помощник. \n'
          'Что Вы хотите сделать? \n'
          '1 - Записать данные \n'
          '2 - Вывести данные')
    command = int(input('Ваш выбор: '))

    while command < 1 or command > 2:
        command = int(input('Ошибка! Ваш выбор: '))

    if command == 1:
        input_data()
    elif command == 2:
        print_data()

interface()