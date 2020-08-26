
#abstract class er object nai
#abstract class ke must base class kore nite hobe,eke jarai inherit korbe tader e abstract method implement kora lagbe
from abc import ABC,abstractmethod

class stu1(ABC):

    @abstractmethod
    def dd(self):
        pass

class stu2(stu1):

    def dd(self):
        print("hi")

obj=stu2()

obj.dd()


