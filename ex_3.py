# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.

def my_func(arg_1, arg_2, arg_3):
    s = [arg_1, arg_2, arg_3]
    s.sort()
    print(s)
    s.remove(min(arg_1, arg_2, arg_3))
    print(s)
    print(s[0] + s[1])

my_func(5, 10, 3)