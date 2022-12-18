class One:
    def __init__(self, name):
        self.name = name
class Two(One):
    def __init__(self, age):
        self.age = age

class Three(Two):
    def __init__(self, name):
        self.name = name

    def n_Hero(self): 
        print("Имя", self.name)

aHero = Three("Sigma")
aHero.n_Hero()



class Four(Three):
    def __init__(self, health_points,):
        self.health_points = health_points
        
    def health(self): 
        print("Здоровье: ",self.health_points ** 2)
 

aHero = Four(100)
aHero.health()



class Five(Four):
    def __init__(self, name, age):
        self.name = name
        self.age = age

aHero = Three("Sigma")
aHero.n_Hero()

aHero = Four(100)
aHero.health()

