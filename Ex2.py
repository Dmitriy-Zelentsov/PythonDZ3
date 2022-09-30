# Напишите программу, которая найдёт произведение пар чисел списка.
#  Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# *Пример:*
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

a = input('Введиите список: ').split()
if len(a) % 2 == 0:
    b = a[len(a):len(a)//2-1:-1]
    print(b)
    c = a[:len(a)//2:]
    print(c)
    bc = [int(b[i])*int(c[i]) for i in range(len(b))]
    print(bc)   
else:
    b = a[len(a):len(a)//2:-1]
    print(b)
    c = a[:len(a)//2:]
    print(c)
    bc = [int(b[i])*int(c[i]) for i in range(len(b))]
    bc.append((int(a[len(a)//2])**2))
    print(bc)

