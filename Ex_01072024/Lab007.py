#Abstructs - which enforce to create method 
from abc import ABC,abstractmethod

class Father(ABC):

    @abstractmethod
    def father_abstruct_method(self):
        print('I am Abc method')

class Son(Father):
    def father_abstruct_method(self):
        super().father_abstruct_method()
        print('I am child')

son = Son()
son.father_abstruct_method()