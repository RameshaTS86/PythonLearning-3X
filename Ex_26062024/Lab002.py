class dog:
    name = None

    def sleep(self):
        print(self.name,'is sleeping..!')

husky = dog()
husky.name = 'Huskey'



dog_list = ['Huskey','Hachiko','JermanSherferd','StreetDog']

for dg in dog_list:
    dg1 = dog()
    dg1.name = dg
    dg1.sleep()
