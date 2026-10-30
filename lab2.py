from csv import reader
import random


# чтение таблицы
def open_table():
    try:  # пробуем выполнить код, чтобы программа не выдала ошибку
        with open('books.csv', 'r') as csvfile:  # r - для чтения
            table = list(reader(csvfile, delimiter=';'))  # reader читает таблицу, list превр ее в список
        return table[1:]  # return - возвращение результата
    except FileNotFoundError:  # если файл не найден
        print('файл не найден')
        return 0  # возвращаем 0, чтобы программа поняла, что файл не открылся


# поиск текста в строке
def find_string(searchline, string):
    return string.lower().find(searchline.lower())  # lower - регистр


# книги с названием длиннее 30 символов
def count_long_names(table):
    count = 0
    for row in table:  # перебираем все книги
        if len(row[1]) > 30:  # len считает количество символов в названии
            count += 1 
    return count  # возвращаем итоговое количество


# 2 поиск книг по автору
def search(table):
    searchline = input('введите имя автора: ')
    if searchline == '':
        return  # завершаем функцию

    flag = 0
    for row in table:
        price = float(row[7])  # float перевод текста в число (даже дробное)

        # проверяем автора и цену книги
        if find_string(searchline, row[3]) != -1 and price >= 200:
            print(row[3], '-', row[1], '- цена', row[7])
            flag += 1

    if flag == 0:
        print('ничего не найдено')
    else:
        print('найдено позиций:', flag)


# 3 20 случайных книг + файл references
def make_references(table):
    chosen = random.sample(table, 20)  # sample отв за уникальность
    output = open('references.txt', 'w', encoding='utf-8')  # w позволяет записывать, encoding отв за кодировку
    number = 1

    for row in chosen:
        year = row[6][6:10]  # для года
        line = f'{number}. {row[3]}. {row[1]} - {year}'  # f позволяет вставлять значения переменных прямо в текст
        print(line)
        output.write(line + '\n')  # write - заипсь текста в файл, \n перенос на новую строку
        number += 1

    output.close() 


# 4 данные из currency.xml
def get_currency():
    with open('currency.xml', 'r') as f:  # открываем файл для чтения
        text = f.read()  # read считывает всё содержимое файла

    num_codes = []
    char_codes = []

    # ищем все числовые коды валют
    pos = 0
    while text.find('<NumCode>', pos) != -1:  # пока find находит открывающий тег
        start = text.find('<NumCode>', pos) + len('<NumCode>')  # находим начало значения после тега
        end = text.find('</NumCode>', start)  # находим позицию закрывающего тега
        num_codes.append(int(text[start:end]))  # int переводит текст в целое число, append добавляет его в список
        pos = end  # продолжаем поиск с новой позиции

    # ищем все буквенные коды валют
    pos = 0
    while text.find('<CharCode>', pos) != -1:  # пока находим буквенный код
        start = text.find('<CharCode>', pos) + len('<CharCode>')
        end = text.find('</CharCode>', start)
        char_codes.append(text[start:end])  # добавляем найденный код в список
        pos = end  # продолжаем поиск дальше

    print('NumCode:', num_codes)
    print('CharCode:', char_codes)


# 5 уникальные теги
def get_tags(table):
    tags = []

    for row in table:  # перебираем все книги
        for tag in row[12].split('#'):  # split разделяет строку на части по решетке
            tag = tag.strip()  # strip убирает пробелы

            # добавляем только новые и непустые теги
            if tag != '' and tag not in tags:
                tags.append(tag)

    tags.sort()  # sort сортировка по алфавиту

    print('колво уникальных тегов:', len(tags))  # len счетчик
    for tag in tags:
        print(tag)


# 6 самые популярные книги
def popular_books(table):
    loans = {}  # словарь 

    for row in table:
        name = row[1]

        # складываем количество продаж одинаковых названий
        if name in loans:  # проверка есть ли книга уже в словаре
            loans[name] = loans[name] + int(row[8])  # добавляем продажи к существующему значению
        else:
            loans[name] = int(row[8])  # если книги еще нет

    # собираем пары из количества продаж и названия
    pairs = []
    for name in loans:
        pairs.append((loans[name], name))  # добавляем пару в список

    pairs.sort(reverse=True)  # сортируем пары по убыванию количества продаж

    print('20 самых популярных книг:')
    for i in range(20):  # повторяем цикл 20 раз
        count, name = pairs[i]  # получаем количество и название из пары
        print(i + 1, name, '-', count, 'выдач')


table = open_table()

if table != 0:  # если таблица загрузилась
    print('1) записей с названием длиннее 30 символов:',
          count_long_names(table))
    print()

    print('2) поиск по автору:')
    search(table)
    print()

    print('3) ссылки (сохранены в references.txt):')
    make_references(table)
    print()

    print('4) данные из currency.xml:')
    get_currency()
    print()

    print('5) уникальные теги:')
    get_tags(table)
    print()

    print('6) самые популярные книги:')
    popular_books(table)
