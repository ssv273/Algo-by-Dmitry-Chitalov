'''
Посчитать четные и нечетные цифры введенного натурального числа. Например, если
введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
'''

# вариант со списками
num = list(input('Введите произвольное число:  '))
even = 0
odd = 0

for el in num:
    if int(el) % 2 == 0:
        even += 1
    else:
        odd += 1
print('Во введенном числе {} четных цифр и {} нечетных'.format(even, odd))


# вариант без
num = input('Введите произвольное число:  ')
even = 0
odd = 0

for el in num:
    if int(el) % 2 == 0:
        even += 1
    else:
        odd += 1
print('Во введенном числе {} четных цифр и {} нечетных'.format(even, odd))