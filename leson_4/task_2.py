# 2 - Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов 
# исходной последовательности. Не использовать множества.
# Постарайтесь решить за одно условие
# [1,1,1,1,2,2,2,3,3,3,4] -> [1,2,3,4]


from typing import List

def show_unique_elements(lst: list) -> list:
    
    lst_new = []
    for i in range(len(lst)):
        if lst[i] not in lst_new:
            lst_new.append(lst[i])
    return lst_new        
  
lst = list(input('Введите элементы через пробел:\n').split())     

try:
    lst_of_numbers = list(map(int, lst))
    print(show_unique_elements(lst_of_numbers))
except ValueError:
    print(show_unique_elements(lst))    
                                                                                                 
