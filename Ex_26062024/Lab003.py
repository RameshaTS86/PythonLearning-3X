#Constructor

class dog:
    name = None
    id = None

    #Constructor Method
    def __init__(self,name,id):
        self.name = name
        self.id = id

    def sleep(self):
        print(self.id,':',self.name, 'is sleeping..!')


#husky = dog('Huskey',1).sleep()
#hachiko = dog('Hachiko',2).sleep()

dog('Huskey',1).sleep()
dog('Hachiko',2).sleep()
dog('Jerman Sh',3).sleep()

