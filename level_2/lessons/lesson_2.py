# когда вы первый раз пушите
# git init
# git remote add origin
# когда вы изменили или хотите запушить
# git add .
# git commit -m 'ваш коммит'
# git push origin master/main

# git rm --cached название файла
# git rm --cached -r название папки


# Объектно ориентированное программирование
# наследование полиморфизм
# git

# супер класс == главный класс
class Human:
    head=1
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return f'name is {self.name}\n' \
               f'age is {self.age}\n'

    def run(self):
        print(f'{self.name} is running')

hum=Human('Sadir',36)
print(hum,hum.head)
# hum.run()

# дочерний класс
class Student(Human):
    head = 2
    def __init__(self, name, age,lastname):
        super().__init__(name, age)
        Human.__init__(self,name,age)
        self.lastname=lastname
    def fly(self):
        print(self.name, 'is fly in True')

    def __str__(self):
        return f'name is {self.name}\n' \
               f'age is {self.age}\n' \
               f'lastname is {self.lastname}\n'

student=Student('Daniyel',60,'Ermekov')

print(student,student.head)
# student.run()
student.fly()

# дочерний класс
class Teacher(Student):
    def fly(self):
        print(f'{self.name} is flying')

tech=Teacher('Beka',55,'DJU')
tech.fly()
# tech.run()