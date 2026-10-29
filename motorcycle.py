class vehicle:
    """base class for all vehicles"""
    
    def __init__(self,nume,manufacturer,color):
        print("creating a vehicle")
        self.name = name 
        self.manuacturer = manufacturer
        self.color = color 
    def drive(self):
        print("driving",self.manuacturer,self.name)
    def turn(self,direction):
        print("turning",self.name,"to",direction)
    def brake(self):
        print(self.name,"is stoping!")
class motorcycle(vehicle):
    """motorcycle class"""
    def __init__(self,wheels,manufacturer,color,year):
        self.manuacturer = manufacturer
        self.color =  color
        self.year = 2014
        self.wheels = 2
        print("A new motorcycle has been created.name:",self.manuacturer)
        print("It has",self.wheels,"wheels")
        print("The motorcycle  was built in",self.year)
    def change_gear(self,gear_name):
        """Method of changing gear"""
        print(self.name,"is changing gear to",gear_name)
        

if __name__ == "__main__":
    c = motorcycle("ford","Kawasaki Ninja H2R ","Red",2014)