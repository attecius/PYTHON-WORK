class Student:
    
    count = 0

    def __init__(self, name,age, roll ):
        self.name = name
        self.age = age
        self.roll = roll
    
    def totalS(self):
        self.count =  self.count+1
        return self.count
    


Student1 = Student("Ajay", 15, 21)

print(Student1.totalS())
Student2 = Student("Vinod", 16, 225)

print(Student1.name)

print(Student2.name, Student2.age, Student2.roll)

print(Student2.totalS())






