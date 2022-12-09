"""1) Напишите функцию, которая принимает фразу, и возвращает его сокращенную
форму.
Например: Кыргызская Республика -- КР. Ruby on Rails -- ROR. For your interest --
FYI и т.п.
2) Напишите функцию, которая проверяет, сколько раз каждое слово в переданной
фразе было использовано. Например: “Money, money, money, it’s always sunny, in
the richmen’s world”. money: 3, it’s: 1, always: 1, sunny: 1, in: 1, the: 1, richmen’s: 1,
world: 1.
3) Напишите функцию, которая принимает слово и возвращает True, если слово
изограмма (т.е. все буквы в слове уникальны). Иначе возвращает False.
4) Напишите функцию где мы передаем через аргументы число n как целое
integer, надо вывести целове число в перевернутом виде
например: n = 27, тогда перевёрнутое n это 72
ДОП ЗАДАНИЕ:
5) Напишите функцию -- чат-бот с бесконечным циклом, который
a. Всегда отвечает “Конечно!” на любой вопрос
b. Всегда отвечает “Успокойся”, если ты кричишь на него ВОТ ТАК!
c. Всегда отвечает “Как классно, когда ты молчишь. Продолжай в том же
духе!” Если вызвал функцию, но ничего не передал.
d. В любых других случаях, отвечает “ну и что" """

# # ex 1 

# def shorter(phrase):
#     phrase_dict = phrase.split()
#     for i in range(len(phrase_dict)):
#         print(phrase_dict[i][0], end = '')

# shorter('Кыргызская Республика')



# # ex 3 

# def unique(word):
#     word_dict =  list(word)
#     no_double = set(word)
#     if len(word_dict) == len(no_double):
#         return True
#     return False
# print(unique('здарова'))
# print(unique('привет'))

# # ex 4 

# def number_reverved(number): 
#     return int(str(number) [::-1])
# print(number_reverved(27))

# ex 5 

# word = input(":")
# def ltr(slowa):
#     if slowa[-1]== "?":
#         return "Конечно!"
#     elif slowa == " ":
#         return "Как классно, когда ты молчишь. Продолжай в том же духе!"
#     elif slowa == "ВОТ ТАК!":
#         return "УСПОКОЙСЯ!!!"
#     else:
#         return "ну и что"
# print(ltr(word))



