import time  # для задержки
import os  # для очистки


BLUE = '\u001b[44m'
RED = '\u001b[41m'
WHITE = '\u001b[47m'
BLACK = '\u001b[40m'
RESET = '\u001b[0m'  
GREEN = '\u001b[42m'
YELLOW = '\u001b[43m'


def flag(k=2, background=WHITE, cross=BLUE):
    pixel = '  ' 
    width = 18 * k  
    height = 11 * k  
    cross_w = height // 3  
    start_vert = width // 3  # начало вертикальной части креста
    start_hor = (height - cross_w) // 2  # начало горизонтальной части

    for y in range(height):  # проходим по всем строкам
        line = ''  
        for x in range(width):  # проходим по всем позициям в строке
            # проверяем, находится ли позиция на кресте
            vertical = start_vert <= x < start_vert + cross_w
            horizontal = start_hor <= y < start_hor + cross_w
            if vertical or horizontal:
                line = line + cross + pixel  # рисуем крест
            else:
                line = line + background + pixel  # рисуем фон
        print(line + RESET) 


def circles(repeats=3):
    pixel = '  ' 
    height = 9  
    width = 17 
    center1_x = 4  
    center2_x = 12  
    center_y = 4  
    radius = 4  

    for y in range(height):  # проходим по строкам
        line = ''
        for x in range(width):  # проходим по позициям в строке
            # проверяем, находится ли точка внутри первого круга
            in_circle1 = (x - center1_x)**2 + (y - center_y)**2 <= radius**2
            # проверяем, находится ли точка внутри второго круга
            in_circle2 = (x - center2_x)**2 + (y - center_y)**2 <= radius**2
            if in_circle1 or in_circle2:
                line = line + BLACK + pixel  # если внутри круга — чёрный цвет
            else:
                line = line + WHITE + pixel  # иначе белый цвет
        print((line + RESET) * repeats)


def animation():
    k = 1  
    height = 11 * k  
    crosses = [BLUE, RED, GREEN, YELLOW]  

    os.system('cls')  # очищаем консоль
    for cross in crosses:  # по очереди берём каждый цвет
        flag(k, WHITE, cross)  # рисуем флаг с выбранным цветом
        time.sleep(1)  
        print(f'\u001b[{height}A', end='')  # поднимаем курсор вверх
    print(f'\u001b[{height}B')  # возвращаем курсор вниз


def sequence():
    file = open('sequence.txt', 'r') 
    first = []  # список для положительных чисел
    second = []  # список для отрицательных чисел
    for line in file:  # читаем файл построчно
        number = float(line)  # превращаем строку в число
        if 5 <= number <= 10:
            first.append(number)  # добавляем число в первую группу
        elif -10 <= number <= -5:
            second.append(number)  # добавляем число во вторую группу
    file.close() 
    # считаем проценты
    percent1 = len(first) / (len(first) + len(second)) * 100
    percent2 = 100 - percent1

    print(BLUE + ' ' * int(percent1) + RESET, round(percent1, 1), '%')
    print(RED + ' ' * int(percent2) + RESET, round(percent2, 1), '%')


def graph(height=9):
    width = height 

    # идём сверху вниз по значениям y
    for y in range(height, 0, -1):
        line = str(y) + '│'  # добавляем значение y и вертикальную ось
        for x in range(1, width + 1):  # проходим по позициям графика
            if x == y:
                line += RED + '  ' + RESET  # ставим точку графика
            else:
                line += '  '  # оставляем пустое место
        print(line)  # выводим строку графика
    print('0└' + '──' * width)  # рисуем горизонтальную ось
    numbers = '  '  # место перед числами на оси x
    for x in range(1, width + 1):
        number = str(x * 2)  # получаем значения x для функции y = x / 2
        if len(number) == 1:
            numbers += number + ' '  # для однозначных чисел добавляем пробел
        else:
            numbers += number  # двузначные числа уже занимают два символа
    print(numbers)  # выводим значения оси x


flag()  
print()  
circles()  
print()  
input('enter - начать анимацию  ')  
animation()  
sequence() 
print()  
graph()  