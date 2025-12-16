from abc import ABC,abstractmethod
class base(ABC):
    def display(self,x):
        self.x=x
        print("hi from parent class")
        print(self.x)
    @abstractmethod
    def show(self):
      pass  
class child(base):
   def show(self):
      print("child class")
c=child()
c.display(123)
c.show()
