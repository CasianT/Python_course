# 5-Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи
# Решение оформлять в виде функций
# По возможности добавляйте docstring


def neg_fibo_pos(number: int) -> list:
    
    
    np_fibo = [0]
    fib1 = 0
    fib2 = 1
    neg = 1
    for i in range(1, number + 1):
        fib1, fib2 = fib2, fib1 + fib2
        np_fibo.append(fib1)
        np_fibo.insert(0, neg * fib1)
        neg *= -1
    return np_fibo    

num = int(input("Задайте число:\n"))
print(neg_fibo_pos(num))   