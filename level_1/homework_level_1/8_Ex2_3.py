"""1) Напишите функцию, которая принимает список, из списка выдает случайное
значение из списка и записывает результат в txt файл. Список language =
["Python", "Java", "Kotlin", "JavaScript", "C#","RUBY"]
2) У нас есть переменная text которая, хранит в себе текст:
Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum
has been the industry's standard dummy text ever since the 1500s, when an unknown
printer took a galley of type and scrambled it to make a type specimen book. It has
survived not only five centuries, but also the leap into electronic typesetting, remaining
essentially unchanged. It was popularized in the 1960s with the release of Letraset
sheets containing Lorem Ipsum passages, and more recently with desktop publishing
software like Aldus PageMaker including versions of Lorem Ipsum.
Откройте файл text.txt и запишите текст в файл 2 способами
ДОП ЗАДАЧА:
3) Написать программу, которая откроет созданный в задаче 2 файл text.txt,
скопирует весь текст и запишет его в новый файл wikipedia.txt ."""

# ex 1 

# import random 

# language = ["Python", "Java", "Kotlin", "JavaScript", "C#","RUBY"]

# f = open('homework_8.txt', 'w')
# f.write(random.choice(language))
# f.close()

# ex 2 

# text = """Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum
# has been the industry's standard dummy text ever since the 1500s, when an unknown
# printer took a galley of type and scrambled it to make a type specimen book. It has
# survived not only five centuries, but also the leap into electronic typesetting, remaining
# essentially unchanged. It was popularized in the 1960s with the release of Letraset
# sheets containing Lorem Ipsum passages, and more recently with desktop publishing
# software like Aldus PageMaker including versions of Lorem Ipsum."""

# # f = open('text.txt', 'w')
# # f.write(text)
# # f.close()

# with open("text.txt", "w") as w:
#     w.write(text)
#     w.close()

# ex 3

# f=open('text.txt')  
# f1=open('wikipedia.txt','a')
# for x in f.readlines():
#     f1.write(x)
# f.close()
# f1.close()