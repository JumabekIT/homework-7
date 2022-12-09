# # Функции 
# def calc():
#     number1 = int(input("Введите первое число: "))
#     number1 = int(input("Введите второе число: "))
#     print(number1 + number2)

# def hello_world():
#     print("Hello World")
#     def test():
#         print("Testing")
#     test()
# hello_world()

# def add(num1, num2):
#     print(num1 + num2)
# add(20, 30)
# add(20, 40)
# add(200, 400)
# add(10, 10)

# def chet(number):
#     if number % 2 == 0:
#         print(number, "Четное")
#     else:
#         print(number, "Нечетное")
# chet()




# def input():
#     print("Hi")
# input()





# def add(num1, num2):
#     return num1 + num2

# def sub(num1, num2):
#     return num1 - num2

# def mult(num1, num2):
#     return num1 * num2

# def div(num1, num2):
#     return num1 / num2

# def main(number1, number2, operator):
#     if operator == "+":
#         return add(number1, number2)
#     elif operator == "-":
#         return sub(number1, number2)
#     elif operator == "*":
#         return mult(number1, number2)
#     elif operator == "/":
#         return div(number1, number2) 
#     else:
#         return "Operator not found"
# print(main(20, 30, "+"))
# print(main(20, 30, "-"))
# print(main(20, 30, "*"))
# print(main(20, 30, "/"))

def number_reverved(number):
    return int(str(number) [::-1])
print(number_reverved(477))

# numbers = ['1', '2', '3', '4']
# res = str().join(numbers)
# print(res)







# def reversed_list(lst : list) -> turple:
#     return turple(reversed(lst))
# print(reversed_list([1, 2, 3, 4]))

# def add(num1, num2):
#     return num1 + num2 
# print(add(10, 60))


# def add(num1 : int = 10, num2 : int = 30): -> int
#     return num1 + num2 
# print(add(30))
