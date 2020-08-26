# protita method e self thakbe must

class student:
    roll=""
    name=""
    def __init__(self,r,n):  # constructor
        self.roll=r
        self.name=n
    def display(self):
        print(self.name)

obj1=student(102,"mita")
obj1.display()
