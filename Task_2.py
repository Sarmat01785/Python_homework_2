"""                        
                                 Задача 12: 
Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. 
Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. 
Помогите Кате отгадать задуманные Петей числа.
"""


S = int(input("Введите сумму чисел: "))
P = int(input("Введите произведение чисел: "))

x, y = None, None

for i in range(1, 1000):
    for j in range(1, 1000):
        if i + j == S and i * j == P:
            x, y = i, j
            break

if x is not None and y is not None:
    print(f"Задуманные числа: {x} и {y}")
else:
    print("Невозможно найти решение.")