'''1) Есть обычная функция
def hello(x):
print(x * x - 10)
Превратите данную функцию в lambda функцию
2) Есть список name = [“Kuma”, “Nurtilek”, “Zina”, “Edzen”, “Kuma”, “Aitenur”, “Zina” ]
Уберите дубликаты с данного листа с помощью lambda функций
3) Есть список numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Выведите с помощью lambda функции чётные числа с списка
4) names = [“azat”, “zina”, “kuma”, “anna”, “sas”]
Вывести с помощью lambda функции имена палиндромы
ДОП ЗАДАЧА:
5) Дайте пользователю ввести две отметки времени вместе с секундами. Ваша
программа должна найти разницу между двумя отрезками времени и вывести
на экран в секундах.
Условие: Первая отметка должна быть раньше по времени чем вторая.**
Пример:
1-ввод: 10:00:30
2-ввод: 15:05:09
Ответ: 18 279 секунд разница'''

# ex 1 

# hello = (lambda x: x * x - 10)
# print(hello(4))

# ex 2 

# name = ["Kuma", "Nurtilek", "Zina", "Edzen", "Kuma", "Aitenur", "Zina" ]

# delete_clons = lambda name : set(name)
# print(delete_clons(name))

# ex 3 

# numbers = [1, 2, 3, 4, 5, 6, 7, 8 , 9, 10]
# res = list(filter(lambda lst_numbers: lst_numbers % 2 == 0, numbers))
# print(res)

# ex 5 

# hour = 7
# first = 30 
# second = 5
# def time(hour, first, second):
#     return f"{hour * 3600 + first * 60 + second}"

# print(time(hour, first, second))