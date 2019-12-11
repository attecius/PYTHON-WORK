class vehicle:

    def __init__(self, tyres, color):
        self.tyres = tyres
        self.color= color
    
    def material(self):
        return "The material is steel"



class car(vehicle):

    def material(self):
        return "The material is aluminum"

    def milage(self):
        return "The milage is 40 "


v1 = vehicle(8 , "red")

v2 = car(4, "black")



print(v1.material())

print(v2.tyres)

print(v2.material())



class audi(car):

    def milage(self):
        return "The milage is 20 "

    def model(self):
        return "A5"


v3 = audi(4, "white")

print(v3.tyres)