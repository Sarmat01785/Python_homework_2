"""                                         
                                           Задача 10: 
На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
Определите минимальное число монеток, которые нужно перевернуть, 
чтобы все монетки были повернуты вверх одной и той же стороной. 
Выведите минимальное количество монет, которые нужно перевернуть
"""



# Вариант 1.
n = int(input("Введите общее кол-во монет: "))
tails = int(input("Введите кол-во монет, которые лежат вверх решкой: "))
emblem = int(input("Введите кол-во монет, которые лежат вверх гербом: "))

if tails > n or tails < 0 or emblem > n or emblem < 0 or tails + emblem > n:
    print("Введено неверное кол-во монет повторите попытку")
else:
    a = n - tails
    b = n - emblem
    if a < b:
        print(f"Минимальное кол-во монет, которые нужно перевернуть: {a}")
    else:
        print(f"Минимальное кол-во монет, которые нужно перевернуть: {b}")


# Вариант 2.
# n = int(input("Введите общее кол-во монет: "))
# tails = int(input("Введите кол-во монет, которые лежат вверх решкой: "))
# emblem = int(input("Введите кол-во монет, которые лежат вверх гербом: "))
#
# if tails > n or tails < 0 or emblem > n or emblem < 0 or tails + emblem > n:
#     print("Введено неверное кол-во монет повторите попытку")
# else:
#     min_1 = float("inf")
#     i = 0
#
#     if tails > emblem:
#         while i <= n:
#             if n - i == tails and i == emblem:
#                 min_1 = i
#                 break
#             i += 1
#     else:
#         while i <= n:
#             if n - i == emblem and i == tails:
#                 min_1 = i
#                 break
#             i += 1
#
#     if min_1 == float("inf"):
#         print("Невозможно найти решение")
#     else:
#         print(f"Минимальное кол-во монет, которые нужно перевернуть: {min_1}")


# Вариант 3.
# n = int(input("Введите общее кол-во монет: "))
# tails = int(input("Введите кол-во монет, которые лежат вверх решкой: "))
# emblem = int(input("Введите кол-во монет, которые лежат вверх гербом: "))
#
# if tails > n or tails < 0 or emblem > n or emblem < 0 or tails + emblem > n:
#     print("Введено неверное кол-во монет повторите попытку")
# else:
#     min_1 = float("inf")
#
#     if tails > emblem:
#         for i in range(n + 1):
#             if n - i == tails and i == emblem:
#                 min_1 = i
#                 break
#     else:
#         for i in range(n + 1):
#             if n - i == emblem and i == tails:
#                 min_1 = i
#                 break
#
#     if min_1 == float("inf"):
#         print("Невозможно найти решение")
#     else:
#         print(f"Минимальное кол-во монет, которые нужно перевернуть: {min_1}")