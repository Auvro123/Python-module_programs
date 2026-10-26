class vehicle:
    """Base class for all vehicles"""
    
    def __init__(self,name,manufacture,color):
        self.name =name
        self.manufacture = manufacture
        self.color = color
        
    def drive(self):
        print("driving",self.manufacture,self.name)
            
    def turn(self,direction):
        print("turning",self.name,"to",direction)
        
    def brake(self):
        print(self.name,"is stoping!")
        
class car(vehicle):
    """car class"""

    def change_gear(self,gear_name):
        """method for changing gear"""
        print(self.name,"is changing gear to",gear_name)
        
if __name__ =="__main__":
    
    c = car("mustang 5.O GT coupe","ford","blue")
    c.drive()
    c.brake()
    c.change_gear("p")