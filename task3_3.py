# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

from random import uniform

n = int(input("Введите размерность списка: "))

if n <= 0:
    raise SystemExit('Ошибка ввода')

numbers = [round(uniform(0, 10), 2) for x in range(n)]
print(numbers)

fractional_parts = []

for i in range(0, n):
    str_number = str(numbers[i])
    pos = str_number.index('.')

    if pos > 0:
        fractional_parts.append(int(str_number[pos+1:]))

print(fractional_parts, max(fractional_parts), min(fractional_parts))
print(f'Результат: {max(fractional_parts) - min(fractional_parts)}')
