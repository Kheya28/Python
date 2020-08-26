
class student:
    roll=""
    name=""
    def setdata(self,r,n):  # protita method e self thakbe must
        self.roll=r
        self.name=n
    def display(self):
        print(self.name)

obj=student()
print(isinstance(obj,student))   #if obj is an object of class student then it will return true
obj.roll=111
obj.name="mita"
print("roll: ",obj.roll," & name: "+obj.name)
obj.display()


obj1=student()
obj.setdata(101,"rima")
obj.display()

