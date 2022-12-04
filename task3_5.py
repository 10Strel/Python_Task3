# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]


def func(n):
    if n > 0:
        if n == 1:
            return [1]
        elif n == 2:
            return [1, 1]

        lst = func(n-1)
        lst.append(lst[-1] + lst[-2])
    else:
        if n == -1:
            return [1]
        elif n == -2:
            return [1, -1]

        lst = func(n+1)
        lst.append(lst[-2] - lst[-1])

    return lst


k = int(input("Введите число: "))

if k <= 0:
    raise SystemExit('Ошибка ввода')

print(list(reversed(func(-k))) + [0] + func(k))