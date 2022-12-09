"""#homework 
дз 2
дедлайн до слующего урока
работать дальше в том же файле с 1 дз

стрим
https://youtu.be/v7EKX4AUxpA

Наследование) 
Создать 3 класса наследованных от класса SuperHero
Все эти классы это герои своей местности(воздушные, земные ,космические и тд)


 к каждому классу добавить 
Свой атрибут на уровне класса.
И новый параметр(конструктора) fly который по УМОЛЧАНИЮ будет равен False

(полиморфизм)
У каждого класса наследованных от Hero
Изменить метод который умножал хп героев на 2
теперь он должен возводить его в квадрат и меняет значение параметра fly на True 

создать новый метод который 
выводит фразу fly in the True_phrase

создать объекты у новых классов
и вызвать новые методы"""


class SuperHero:
    people = 'people'
    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name 
        self.nickname = nickname 
        self.superpower = superpower 
        self.health_points = health_points 
        self.catchphrase = catchphrase
    def n_Hero(self): 
        print("Имя героя", self.name)

    def health(self): 
        print("Здоровье: ",self.health_points * 2)

    def __str__(self) -> str: 
        return f"Status hero : \nПсевдоним - {self.nickname}\nСпособность - {self.superpower}\nЗдоровье - {self.health_points}" 
         
    def __len__(self): 
        return len(self.catchphrase)

hero = SuperHero('Thor', 'Odinson', 'Flying', 100, 'For Asgard')
hero.n_Hero() 
hero.health() 
print(hero) 
print(len(hero))


#################################################



class AirHero(SuperHero):
    fly = False
    def __init__(self, health_points, fly = False):
        self.health_points = health_points
        self.fly = fly

    def health(self): 
        print("Здоровье: ",self.health_points ** 2)


    def phrase(self):
        self.fly = True
        print("fly in the True_phrase", self.fly)
    

aHero = AirHero(100)
aHero.health()
aHero.phrase()





class EarthlyHero(SuperHero):
    fly = False
    def __init__(self, health_points, fly = False):
        self.health_points = health_points
        self.fly = fly

    def health(self): 
        print("Здоровье: ",self.health_points ** 2)
        fly = True

    def phrase(self):
        self.fly = True
        print("fly in the True_phrase", self.fly)

aHero = AirHero(100)
aHero.health() 
aHero.phrase()


class SpaceHero(SuperHero):
    fly = False
    def __init__(self, health_points, fly = False):
        self.health_points = health_points
        self.fly = fly

    def health(self): 
        print("Здоровье: ",self.health_points ** 2)
        fly = True

    def phrase(self):
        self.fly = True
        print("fly in the True_phrase", self.fly)

aHero = AirHero(100)
aHero.health() 
aHero.phrase()
