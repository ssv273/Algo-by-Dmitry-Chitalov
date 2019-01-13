'''
Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...Количество элементов
(n) вводится с клавиатуры.
'''

n = int(input('Введите количество элементов '))
lst = [1]
for i in range(n - 1):
    lst.append(lst[i] / (-2))
print(sum(lst))

# или
summ = 0
k = 0
for i in range(n):
    if k == 0:
        k = 1
        summ = 1
    else:
        k = k / (-2)
        summ = summ + k
print(summ)
