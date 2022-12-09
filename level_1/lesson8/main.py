# f = open('geektech.txt', 'w')
# f.write("Hello World")
# f.close()

# r = open('geektech.txt', 'r')
# print(r.read())
# r.close()

# code = open('C:/Users/ASUS/Desktop/mycode/lesson7/lesson_7.py', 'r')
# print(code.read())
# code.close()

# pyt = open('hello.py', 'w')
# pyt.write("print('Hello World')")
# pyt.close()

# student = open('student.txt', 'w')
# student.write('Askhat\n')
# student.write('Daniel\n')
# student.close()

# student_1 = open('student.txt', 'a+')
# student_1.write('Almaz')
# student_1.close()

# with open('python.txt', 'w') as f:
#     f.write("Python 3.8.10")

# with open('python.txt', 'r') as r:
#     print(r.read())

import os

# n = 0
# while True:
#     n += 1
#     if n == 10:
#         break
#     else:
#         with open(f'python_{n}.py', 'w') as f:
#             f.write("Hello World")

# n = 0 
# while True:
#     n += 1
#     if n == 1000:
#         break
#     else:
#         os.remove(f'python_{n}.py')




# from datetime import datetime now = datetime.now() current_time = now.strftime("%H:%M:%S") print("Current Time =", current_time)
# import time  

# t = time.localtime() 
# current_time = time.strftime("%H:%M:%S", t) 
# print(current_time)




# def write_login_password(login : str,password : str) -> None:
#     with open('password.txt','w') as o:
#         o.write(f'{login} {password}')

# write_login_password('geektech', 'geektech2021')
# ###########################
# def read_login_password(login : str, password : str) -> bool:
#     with open('password.txt', 'r') as r:
#         result = r.read().split
#     print(result)
#     if login == result[0] and password == result[1]:
#         # logs
#         with open('logs.txt', 'a+') as logs:
#             logs.write(f'{login.lower()} {time.ctime()}\n')
#         return True
#     else:
#         return False

# print(read_login_password('geektech', 'geektech2021'))
# print(read_login_password('geektech', 'geektech2021'))

import random 

def generate_passwords() -> str:
    letters = "qwertyuiopasdfghjklzxcvbnm1234567890"
    res = []
    password = []
    for i in letters:
        res.append(i)
    print(res)
    print(random.choices(res))
    for n in range(10):
        password = []
        for i in range(8):
            password.append(random.choices(res))
            with open('generated.txt', 'a+') as p:
                p.write(f'{"".join(password)}\n')

generate_passwords()