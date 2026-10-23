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
        
        
if __name__ =="__main__":
    
    v1 =vehicle("fusion 110ex","lamborghini","red")
    v2 = vehicle("sofail delux","shongi","blue")
    v3 =vehicle("mustang 5.O GT coupe","ford","yellow")
     
    v1.drive()
    v2.drive()
    v3.drive()
    
    v1.turn("left")
    v2.turn("right")
    
    v1.brake()
    v2.brake()
    v3.brake()