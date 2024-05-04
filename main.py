from pprint import pprint
from glob import glob
import os

def count_ingredients(persons: int, *dishes: tuple) -> dict:
    '''
    Задача №2. Функция подсчета необходимого количества ингредиентов 
    для приготовления введенных блюд на некоторое количество голодных персон
    '''
    total, missing = {}, []
    print(f'\nЗадача: для {persons} человек приготовить каждому {", ".join(dishes)}')
    for dish in dishes:
        if dish in cook_book:
            for ingredients in cook_book[dish]:
                if ingredients['ingredient'] in total:
                    total[ingredients['ingredient']]['quantity'] += int(ingredients['quantity'])*persons
                else:
                    total[ingredients['ingredient']] = {'measure': ingredients['measure'], 
                                                        'quantity': int(ingredients['quantity'])*persons}     
        else:
            missing.append(dish)
    if len(missing):
        print(f"Блюдо(а) {', '.join(missing)} в кулинарной книге отсутствуют, такое не готовим")
    return total

def create_cook_book(external_file: str) -> dict:
    '''
    Задача №1. Функция формирования словаря-кулинарной книги из файла
    '''
    cook_book = {}
    number_of_lines = 0
    with open(external_file, encoding='utf-8') as internal_file:
        for line in internal_file:
            line = line.strip()
            if line == '':
                continue
            elif line.isdigit():
                number_of_lines = int(line)
            elif number_of_lines == 0:
                cook_book[line], key = [], line
            else:
                line = [i.strip() for i in line.split('|')]
                cook_book[key].append({'ingredient': line[0], 
                                       'quantity': line[1], 
                                       'measure': line[2]})
                number_of_lines -= 1
    return cook_book

def union_files(direct):
    '''
    Задача №3. Функция объединения файлов в принимаемой директории с учетом 
    сортировки файлов по возрастанию количества в них строк
    '''
    if os.path.exists(direct):
        lines_list = []
        source_files = glob(os.path.join(direct, '*.txt'))
        source_files = [file for file in source_files 
                        if file != 'union\\solution.txt']    
    for file in source_files:
        file_name = file.split('\\')[1]
        with open(file, encoding='utf-8') as fr:
            lines_list.append((fr.readlines(), file_name))
    lines_list = sorted(lines_list, key=lambda x: len(x[0]))
    with open(r'union\solution.txt', 'w', encoding='utf-8') as fw:
        for lines, file_name in lines_list:
            fw.write(f'{file_name}\n{len(lines)}\n')
            line = [f'Строка №{pos+1} файла №{file_name[0]} {line}' 
                    for pos, line in enumerate(lines)]
            line.append('\n')
            fw.write(''.join(line))



cook_book = create_cook_book('recipes.txt')
print(f'\nСформированная из файла кулинарная книга:\n{"*"*41}')
pprint(cook_book, width=100)

list_for_shopping = count_ingredients(3, 'Утка по-пекински', 'Омлет', 'Гречка', 'Гороховый суп')
print(f'Итоговый список ингредиентов, которые нужно купить:\n{"*"*51}')
pprint(list_for_shopping)

union_files('union')
print(f'\nСформированный и отсортированный документ, ' 
      f'собранный из файлов, располагаемых в директории \\union, '
      f'доступен по ссылке union\\solution.txt\n')