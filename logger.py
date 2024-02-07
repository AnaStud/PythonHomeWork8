from data_create import input_user_data
import itertools

def input_data():
    name, surname, phone, adress = input_user_data()
    var = int(input(f'\nВ каком формате записать данные? \n'
                    f'1 Вариант:\n'
                    f'{name}\n'
                    f'{surname}\n'
                    f'{phone}\n'
                    f'{adress}\n\n'
                    f'2 Вариант:\n'
                    f'{name};{surname};{phone};{adress}\n\n'
                    f'Ваш выбор: '))
    if var == 1:
        with open('data_first_variant.csv', 'a', encoding='utf-8') as file:
            file.write( f'{name}\n'
                        f'{surname}\n'
                        f'{phone}\n'
                        f'{adress}\n\n')
    else:
        with open('data_second_variant.csv', 'a', encoding='utf-8') as file:
            file.write(f'{name};{surname};{phone};{adress}\n\n')


def print_data():
    print('1 файл:')
    with open('data_first_variant.csv', 'r', encoding='utf-8') as file:
        data = file.readlines()
        print(''.join(data))
        
    print('2 файл:')
    with open('data_second_variant.csv', 'r', encoding='utf-8') as file:
        data = file.readlines()
        print(''.join(data))

def copy_data():
    
    n_zap = int(input('Введите номер записи: '))

    with open('data_first_variant.csv', 'r', encoding='utf-8') as file1:
        lines = file1.readlines()[(n_zap-1) * 5:(n_zap) * 5 - 1]
        
        name = lines[0][:-1]
        surname = lines[1][:-1]
        phone = lines[2][:-1]
        adress = lines[3][:-1]
            
        with open('data_second_variant.csv', 'a', encoding='utf-8') as file2:
            file2.write(f'{name};{surname};{phone};{adress}\n\n')