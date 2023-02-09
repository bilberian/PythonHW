# Напишите программу для нахождения максимального числа ягод, 
# которое может собрать за один заход собирающий модуль, 
# находясь перед некоторым кустом заданной во входном файле грядки.

n = int(input('Введите размер грядки: '))
list_1 = list()
max_num = 0
berries_count = 0

for i in range(n):
    b = int(input(f'Введите кол-во ягод на {i + 1}-м кусте грядки: '))
    list_1.append(b)

for i in range(len(list_1) - 1):        # почему не i in list_1? - тогда будут выводиться элементы списка, не индексы
    if i == 0:
        berry_1 = list_1[0] + list_1[1] + list_1[-1]
        if berry_1 > max_num:
            max_num = berry_1
    elif i == len(list_1) - 1:
        berry_last = list_1[-1] + list_1[-2] + list_1[0]
        if berry_last > max_num:
            max_num = berry_last
    else:
        berries_count = list_1[i] + list_1[i-1] + list_1[i+1]
        if berries_count > max_num:
            max_num = berries_count

print(max_num)
