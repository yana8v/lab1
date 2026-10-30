from csv import reader
import random


# чтение таблицы
def open_table():
    try:
        with open('books.csv', 'r') as csvfile:
            table = list(reader(csvfile, delimiter=';'))
        return table[1:]
    except FileNotFoundError:
        print('файл не найден')
        return 0


# поиск
def find_string(searchline, string):
    return string.lower().find(searchline.lower())


# книги с названием длиннее 30 символоы
def count_long_names(table):
    count = 0
    for row in table:
        if len(row[1]) > 30:
            count += 1
    return count


# 2 поиск книг по автору
def search(table):
    searchline = input('введите имя автора: ')
    if searchline == '':
        return

    flag = 0
    for row in table:
        price = float(row[7])
        if find_string(searchline, row[3]) != -1 and price >= 200:
            print(row[3], '-', row[1], '- цена', row[7])
            flag += 1

    if flag == 0:
        print('ничего не найдено')
    else:
        print('найдено позиций:', flag)


# 3 20 рандом книг + файл референсес
def make_references(table):
    chosen = random.sample(table, 20)
    output = open('references.txt', 'w', encoding='utf-8')
    number = 1
    for row in chosen:
        year = row[6][6:10]  # год в дате стоит на позициях 6-9
        line = f'{number}. {row[3]}. {row[1]} - {year}'
        print(line)
        output.write(line + '\n')
        number += 1
    output.close()


# 4 данные из currency.xml
def get_currency():
    with open('currency.xml', 'r') as f:
        text = f.read()  # читаем весь файл одной строкой

    num_codes = []
    char_codes = []

    # ищем все NumCode, пока они есть в тексте
    pos = 0
    while text.find('<NumCode>', pos) != -1:
        start = text.find('<NumCode>', pos) + len('<NumCode>')
        end = text.find('</NumCode>', start)
        num_codes.append(int(text[start:end]))
        pos = end

    # то же самое для CharCode
    pos = 0
    while text.find('<CharCode>', pos) != -1:
        start = text.find('<CharCode>', pos) + len('<CharCode>')
        end = text.find('</CharCode>', start)
        char_codes.append(text[start:end])
        pos = end

    print('NumCode:', num_codes)
    print('CharCode:', char_codes)


# 5 теги
def get_tags(table):
    tags = []
    for row in table:
        for tag in row[12].split('#'):  # теги разделены решеткой
            tag = tag.strip()
            if tag != '' and tag not in tags:
                tags.append(tag)
    tags.sort()
    print('колво уникальных тегов:', len(tags))
    for tag in tags:
        print(tag)


# 6 самые популярные книги
def popular_books(table):
    # словарь: название книги -> сколько раз ее выдавали
    loans = {}
    for row in table:
        name = row[1]
        if name in loans:
            loans[name] = loans[name] + int(row[8])
        else:
            loans[name] = int(row[8])

    # превращаем словарь в список пар (выдачи, название) и сортируем
    pairs = []
    for name in loans:
        pairs.append((loans[name], name))
    pairs.sort(reverse=True)

    print('20 самых популярных книг:')
    for i in range(20):
        count, name = pairs[i]
        print(i + 1, name, '-', count, 'выдач')


table = open_table()

if table != 0:
    print('1) записей с названием длиннее 30 символов:', count_long_names(table))
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