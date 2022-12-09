# def chet(number : int  = 0) -> bool:
#     if number % 2 == 0:
#         return True
#     else:
#         return False 
# print(chet(3))

# lambda_chet = lambda number : number % 2 == 0
# print(lambda_chet(3))

# def while_true():
#     while_True:
#         name = input("Ваше имя: ")
#         print(name)

# def lambda_function():
#     numbers = [1, 2, 3, 4, 5, 6, 7, 8]
#     return list(filter(lambda x: x % 2 == 0, numbers))
# # print(lambda_function())

# num1 = 10
# num2 = 20
# number = 13
# def nearer_number(num1, num2, number):
#     num1_abs = abs(number - num1)
#     num2_abs = abs(number - num2)
#     # if num1_abs < num2_abs:
#     #     return num1
#     # elif num2_abs < num1_abs:
#     #     return num2
#     # else:
#     #     return "Равны"
#     return num1 if num1_abs < num2_abs else num2 if num2_abs < num1_abs else "Равны"
# print(nearer_number(num1, num2, number))

# # print(abs(-10))

# def count_words(words : str):
#     split_words = words.replace("," "").lower().split()
#     res = {}
#     for word in split_words:
#         res[word] = split_words.count(word)
#     return res

# print(count_words("Money, money, money, it's always sunny, in the richmen's world"))



