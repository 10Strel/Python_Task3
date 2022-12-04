# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint

n = int(input("Введите размерность списка: "))

if n <= 0:
    raise SystemExit('Ошибка ввода')

numbers = [randint(0, 100) for x in range(n)]
print(numbers)

sum = 0
for i in range(len(numbers)):
    if i % 2 != 0:
        sum += numbers[i]

print(f'Результат: {sum}')
