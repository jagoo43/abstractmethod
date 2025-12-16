from abc import ABC,abstractmethod
class base(ABC):
    def display(self,x):
        print("hi from parent class")
        print(x)
    @abstractmethod
    def show(self):
      pass  
class child(base):
   def show(self):
      print("child class")
c=child()
c.display(123)
c.show()      

