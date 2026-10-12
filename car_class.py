class car:
    name = ""
    color=""
    def start():
        print("starting the engine ")
car.name ="farari"
car.color ="red"
print("Name of the car:",car.name)
print("color:",car.color)
car.start()

class car:
    name=""
    color=""
    def start():
        print("starting the engine")
my_car = car()
my_car.name ="rolls royce"
print(my_car.name)



class car:
    name=""
    color=""
    def start(self):
        print("starting the engine")
my_car = car()
my_car.name ="rolls royce"
print(my_car.name)

class car:
    name = ""
    color= ""

    def __init__(self,name,color):
        self.name =name
        self.color =color
    def start(self):
        print("starting the engine")
my_car=car("corolla","white")
print(my_car.name)
print(my_car.color)

class car:
    def __init__(self,n,c):
        self.name =n
        self.color =c

    def start(self):
        print("Name :",self.name)
        print("color :",self.color)
        print("starting the engine")

my_car1 =car("corolla","white")
my_car1.start()
my_car2 =car("farari","red")
my_car2.start()
my_car3 = car("rolls royce","black")
my_car3.start()

class car:
    def __init__(self,n,c):
        self.name =n
        self.color =c
    def start(self):
        print("starting the engine")
car =car("corolla","white")
car.year =2017
print(car.name,car.color,car.year)