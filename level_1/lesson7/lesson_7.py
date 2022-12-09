# def mult(num1 : int, num2 : int) -> int:
#     return num1 * num2
# # print(mult(20, 20))

# def div(num1 : int, num2 : int) -> float:
#     try:
#         return num1 / num2
#     except:
#         return "Деление на ноль"
# # print(div(10, 0))

# it = "GeekTech"
# numbers = [10, 20, 30, 40, 50]
# number = 415
# name = "Kurmanbek"

import random
# print(random.randint(1, 5))
def random_number():
    num_random = random.randint(1, 10)
    n = 0
    while True:
        try:
            user_input = int(input("Введиете число от 1 до  10: "))
            if user_input >= 1 and user_input <= 10:
                n += 1
                if num_random == user_input:
                    print(f"Правильный ответ. Число {num_random}")
                    break
                elif n == 5:
                    print("Попытки закончились")
                    break
                else:
                    print(f"Неправильно {5 - n} попыток")
        except ValueError:
            print("Ввкдите целое число")
# random_number()
raise ImportError("ПРивет мир")