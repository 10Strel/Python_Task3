# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

from random import randint

n = int(input("Введите размерность списка: "))

if n <= 0:
    raise SystemExit('Ошибка ввода')

numbers = [randint(0, 10) for x in range(n)]
print(numbers)

first_index = 0
last_index = n-1
res = []

for i in range(0, n // 2 + n % 2):
    res.append(numbers[first_index] * numbers[last_index])
    print(f'i {i}, first_index {first_index}, numbers[first_index] {numbers[first_index]}, last_index {last_index}, numbers[last_index] {numbers[last_index]}')
    first_index += 1
    last_index -= 1

print(res)
