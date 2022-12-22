# 1 - Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# N = 20 -> [2,5]
# N = 30 -> [2, 3, 5]




n = int(input("Введите число: "))
factors = []
d = 2
m = n 
while d * d <= n:
        if n % d == 0:
            factors.append(d)
            n//=d
        else:
            d += 1
factors.append(n) 
print('{} = {}' .format(m, factors)) 
