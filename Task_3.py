"""
                                       Задача 14: 
Требуется вывести все целые степени двойки (т.е. числа вида 2**k), не превосходящие числа N.
"""

N = int(input("Введите число N: "))

count = 0
Degree_of_two = 1

while Degree_of_two <= N:
    print(Degree_of_two)
    count += 1
    Degree_of_two = 2**count

