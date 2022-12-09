# Операторы сравнения, функция input(), условия if else, boolean, циклы
#  ==, >=, <=, <, >, !=
# print(10 == 9)
# print(10 ==10)
# print("IT" == "IT")
# print(10.0 == 10.0)
# print(2 == 2.0)
# print(True == True)
# print(10 == "10")
# print(int("10") == 10)
# print(10 > 20)
# print(10 < 5)
# print(10 != 9)
# print(1000 != 1000)
# print(50 >= 50)
# print(100 >= 50)
# print(30 >= 100)
# print(30 <= 400)

# num1 = int(input("Введите число: "))
# num2 = int(input("Введите второе число: "))
# print(num1 + num2)

# name = input("Введите имя:")
# print("здраствуйте", name)

# if, else, elif
# if True:
    # print("if True")
    # else: 
    #     print("if False")
# num1 = int(input("Введите первое число: "))    
# num2 = int(input("Введите второе число: "))
# if num1 > num2:
#     print("Певрое число больше")
# else: 
#     print("Второе число больше")

# num = int(input("Введите число: "))
# if num % 2 == 0:
#     print(num, "Четный")
# else:
#     print(num, "Нечетный")

# логические операторы or и and

# num1 = 100
# num2 = 100
# num3 = 100
# if num1 > num2 and num1 > num3:
#     print("Первое число больше")
# elif num2 > num1 and num2 > num3:
#     print("Второе число больше")
# elif num3 > num1 and num3 > num2:
#     print("Третье число больше")
# else:
#     print("Они равны")

# login = input("Введите логин: ")
# password = input("Введите парооль: ")
# if login == "geektech" or password == "geektech2021":
#     print("Welcome")
# else:
#     print("Error")

# login = input("Введите логин: ")
# password = input("Введите парооль: ")
# if login == "geektech":
#     if password == "geektech2021":
#         print("Добро пожаловать")
#     else:
#         print("Пароль не совпадает")
# else:
#     print("Неверный логин")
 
# while True: 
#     number1 = float(input("Введите первое число: "))
#     number2 = float(input("Введите второе число: "))
#     operator = input("+, -, *, /: ")
#     if operator == "+":
#         print(number1 + number2)
#     elif operator == "-":
#         print(number1 - number2)
#     elif operator == "*":
#         print(number1 * number2)
#     elif operator == "/":
#         print(number1 / number2)
#     else:
#         print("error")

# print(True + False)

#  циклы for и while

# for num in range(1001):
#     print(num)

# name = "erjan"
# for i in name:
#     if i == "a":
#         print("в имени есть буква а")