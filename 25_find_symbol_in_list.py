Напишите программу, которая считывает список чисел lst из первой строки и число x из второй строки, 
которая выводит все позиции, на которых встречается число x в переданном списке lst

Позиции нумеруются с нуля, если число x не встречается в списке, вывести строку "Отсутствует" (без кавычек, с большой буквы).

Позиции должны быть выведены в одну строку, по возрастанию абсолютного значения.

# put your python code here
lst  = [int(i) for i in input().split()]
x = int(input())
c = []
for i in range(0, len(lst)):
    if x == lst[i]:
        c.append(i)
if len(c) != 0:
    for i in range(len(c)):
        print(c[i], end =' ') 
else:
        print('Отсутствует')
