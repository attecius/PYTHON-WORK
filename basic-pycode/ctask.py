class shape:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    # def square(self,side):    
    #     self.side=side

class square(shape):
    def area(self):
        area =self.length*self.length
        return area

class rect(shape):
    def area(self):
        a=self.length*self.breadth
        return a

v1 =rect(4,3)
print(v1.area())
v2 = square(4,4)
print(v2.area())



 i var account
 wid Dep 
 1000
 1000