from abc import ABC,abstractmethod
class base(ABC):
    def display(self):
        print("hi from parent class")
    @abstractmethod
    def show(self):
      pass  
class child(base):
   def show(self):
      print("child class")
c=child()
c.display()
c.show()