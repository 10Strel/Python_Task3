# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

def decimalToBinary(n):
    if (n > 1):
        decimalToBinary(n // 2)
    print(n % 2, end='')

    
flag = False
while not flag:
    char = input('\r\nВведите число (для выхода нажмите q): ')

    if char == 'q':
        flag = True
        break

    if (not char.isdigit()):
       continue
   
    number = int(char)

    if (number < 0):
        continue

    decimalToBinary(number)
    
    

    