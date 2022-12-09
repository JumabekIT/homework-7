# ex 1

it_company = ('Google', 'Amazon', 'Microsoft') 
print(it_company)

it_company = list(it_company)
print(it_company)

it_company.append('Tesla')
print(it_company)

it_company = tuple(it_company)
print(it_company)

# ex 2

print(it_company.index('Amazon'))

# ex 3 

it_company = list(it_company)
it_company[0] = 'Apple' 
print(it_company)

# ex 4 

print(it_company[0:2])

# ex 5 

text_tuple = ('''Experienced', 'programmers', 'in', 'any', 'other', 'language',
'can', 'pick', 'up', 'Python', 'very', 'quickly,', 'and', 'beginners', 'find', 'the', 'clean',
'syntax', 'and', 'indentation', 'structure', 'easy', 'to', 'learn.', 'Whet', 'your', 'appetite',
'with', 'our', 'python', '3', 'overview''') 
print(text_tuple.count('python')) + print(text_tuple.count('Python'))

# ex 6 

dictionary_1 = {'a': 300, 'b': 400} 
dictionary_2 = {'c': 500, 'd': 600}
dictionary_1.update(dictionary_2)
print(dictionary_1) 

# ex 7 

numbers = {'num)_1' : 1, 'num_2' : 2, 'num_3' : 3, 'num_100' : 100} 
result = 1
for key in numbers:
    result = result * numbers[key]
print(result)

#  ex 8 

student = {'name' : 'Askhat', 'age' : 17}
a = student['age'] * 2
print(a)

# ex 9 

student = {'name' : 'Askhat', 'age' : 17, 'color' : 'White'}
student['age'] = 16
print(student)

#  ex 10 

student = {'name' : 'Askhat', 'age' : 17}
student.pop('age')
print(student)

#  ex 11 

student = {'name' : 'Askhat'} 
student.setdefault('adress', 'Западный Анар')
print(student)

# ex 12 

password = input("Введите пароль: ")
repassword = input("Подтвердите пароль: ")
a = 0 
while a == 0:
    if len(password) < 8:
        print("Короткий")
        password = input("Введите новый пароль: ")
        repassword = input("Подтвердите пароль: ")
    elif "123" in password:
        print("Простой пароль!")
        password = input("Введите новый пароль: ")
        repassword = input("Подтвердите пароль: ")
    elif password != repassword:
        print("Различаются.")
        password = input("Введиет пароль еще раз: ")
        repassword = input("Подтвердите пароль: ")
    else:
        print("OK")
        a += 2
