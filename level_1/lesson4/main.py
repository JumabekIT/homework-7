# Turple - кортеж
# numbers = [1, 2, 3, 4, 5, 6]
# numbers.append(7)
# print(numbers)
# numbers.remove (2)
# print(numbers)
# numbers[0] = "One"
# print(numbers)

# numbers = (1, 2, 3, 4, 5)
# for n in numbers:
#     print(n)
# print(numbers)
# numbers.append(30)
# print(numbers)
# numbers.remove(1)
# print(numbers)
# del numbers[0]
# print(numbers)
# numbers[0] = "One"
# print(numbers)
# print(numbers[0:3:2])
# print(numbers.count(3))
# print(numbers.index(3))

# cities = ["Osh", "Bishkek", "Talas"]
# tup_cities = tuple(cities)
# print(tup_cities)
# lst_cities = list(tup_cities)
# print(lst_cities)
# lst_cities.append("Naryn")
# tup_cities = tuple(lst_cities)
# print(tup_cities)

# Множества set, frozenset
# a = [1, 3, 4, 5]
# b = [4, 5, 6, 7]
# print(list(set(a + b)))

# st = {1, 1.0, True, "1", (1, 2, 3)}
# print(st)
# cars = {"BMW", "LEXUS", "TOYOTA", "BMW"}
# for car in cars:
#     print(car)
# print(cars)
# cars.add("Ferrari")
# print(cars)
# cars.remove("BMW")
# print(cars)
# cars.pop()
# print(cars)

# numbers = {10, 20, 30, 40, 40}
# frzn_numbers = frozenset(numbers)
# print(frzn_numbers)

# Dict - Словари
# n = {1, 2, 3, 4, 5}
# print(len(n))
# student = {'name' : 'Kurmanbek', 'age' : 18}
# print(student)
# print(len(student))
# print(student['name'])
# print(student['age'])
# student.setdefault('work', "GeekTech")
# print(student) 
# print(student.pop('age'))
# print(student) 
# print(student.keys()) 
# print(student.values())
# print(student.items()) 
# student['age'] = 10
# student['test'] = 10
# print(student)
# del student['test']
# print(student)
# for k, v in student.items():
#     print(k, v)

contact = {"MCHS" : 112,}
while True:
    command = input("1 - посмотреть все контакты, 2 - дoбавить контакт, 3 - удалить контакт, 4 - обновить контакт: ")
    if command == "1":
        for name, number in contact.items():
            print(name, number)
    elif command == "2":
        add_name = input("Введите имя которое вы хотите добавить: ")
        add_number = input("Введите номер который вы хотите добавить: ")
        contact.setdefault(add_name, add_number)
        print("Контакт успешно добавлен")
    elif command == "3":
        delete_contact = input("Введите имя которое вы хотите удалить: ")
        if delete_contact  in contact.keys():
            del contact[delete_contact]
            print("Контакт успешно удален")
        else:
            print("Контакт не найден")
    elif command == "4":
        old_contact = input("Введите контакт который хотите обновить: ")
        if old_contact in contact.keys():
            del contact[old_contact]
            print("Контакт найден")
            new_contact = input("Новое имя контакта: ")
            new_number = input("Новый номер контакта: ")
            contact.setdefault(new_contact, new_number)
            print("Контакт успешно обновлен")
        else:
            print("Контакт не найден")


       