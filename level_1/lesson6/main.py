# Лямбдя функции, исключения try, except
# def hello_world():
#     return "Hello World"
# print(hello_world())

# def mult(num):
#     return num * num
# print(mult(10))

# lambda_mult = lambda num: num * num 
# print(lambda_mult(10))

# print((lambda num: num * num)(10))

# def add(num1 : int, num2 : int) -> int:
#     return num1 + num2
# print(add(20, 50))

# lambda_add = lambda num1, num2: num1 + num2
# print(lambda_add(20, 50))

# print((lambda num1, num2: num1 + num2)(20, 50))

# def geek(word):
#     return word
# print(geek("GeekTech"))

# lmd_geek = lambda word: word
# print(lmd_geek("Lambda GeekTech"))

# print((lambda word: word)("print Lambda"))

# numbers = [10, 20, 30, 40, 50]
# def mult_two(lst : list) -> list:
#     res = []
#     for i in lst:
#         res.append(i * 2)
#     return res
# print(mult_two(numbers))
# ############################
# numbers = [10, 20, 30, 40, 50] 
# res = list(map(lambda lst: lst * 2, numbers))
# print(res)
# ###########################
# numbers = [10, 20, 30, 40, 50]
# print(list(map(lambda lst: lst * 2, numbers)))
# ###########################
# print(list(map(lambda lst: lst * 2, [10, 20, 30, 40, 50])))

# nums = [1, 2, 3, 4, 5, 6, 7, 8 , 9, 10]
# def chet(lst_nums: list) -> str:
#     res = []
#     for num in lst_nums:
#         if num % 2 == 0:
#             res.append(num)
#         else:
#             pass
#         return res
# print(chet(nums))
# ######################################
nums = [1, 2, 3, 4, 5, 6, 7, 8 , 9, 10]
res = list(filter(lambda lst_nums: lst_nums % 2 == 0, nums))
print(res)
# #######################
# print(list(filter(lambda lst_nums: lst_nums % 2 == 0, [1, 2, 3, 4, 5, 6, 7, 8 , 9, 10])))

# try:
#     print(10 / 0)
# except ZeroDivisionError:
#     print("Деление на ноль")

# while True:
#     try:
#         num1 = int(input("Введите первое число: "))
#         operator = input("+, -, *, /: ")
#         num2 = int(input("Введите второе число: "))
#         if operator == "+":
#             print(num1 + num2)
#         elif operator == "-":
#             print(num1 - num2)
#         elif operator == "*":
#             print(num1 * num2)
#         elif operator == "/":
#             try:
#                 print(num1 / num2)
#             except ZeroDivisionError:
#                 print("Ошибка на ноль. Учи математику")
#         else:
#             print("Оператор не найден")
#     except ValueError:
#         print("Введите число")
