'''
Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
Вывести на экран это число и сумму его цифр.
'''
# устал я без списков

a = '456 87444 52268 525 25245 252255 2252 62253 25622 522236'
lst = a.split()
max_summ = 0
for i in lst:
    if sum(map(int, (list(i)))) > max_summ:
        max_summ = sum(map(int, (list(i))))
        number = i
print('Среди введенных чисел {}\n наибольшая сумма цифр {} у числа {}'.format(a, max_summ, number))
