#OOPs Concepts
class Person:
    #Attributes
    Name = None
    Id = None
    Age = None
    Phone_Number = None

    #Behavior

    def walk(self):
        print(self.Name,'is Walking')
    def talk(self):
        print(self.Name,'is Talking')

    def sleep(self):
        print(self.Name,'is Slepping')

    def sing(self):
        print(self.Name,'is Singin')


#Objects Creation for above Class
#ObjectReference = Object ->Class Name

Ramesh = Person()
Ramesh.Name = 'Ramesha T S'
Ramesh.Id = 8696
Ramesh.Age = 27
Ramesh.Phone_Number = 7022462927



dog_list = ['Ramesh','Bhoomika','Riyank','Riya']

for prsn in dog_list:
    prsn1 = Person()
    prsn1.name = prsn
    prsn1