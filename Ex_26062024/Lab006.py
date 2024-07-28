class Calculator:

    def __init__(self,a= 1,b=1):
        self.a = int(input('Please Enter a Number1 : '))
        self.b = int(input('Please Enter a Number2 : '))
    def sum(self):

        print('Sum is :',self.a+self.b)

    def diff(self):
        print('Diff is :',self.a-self.b)

    def Mul(self):
        print('Mul is :',self.a*self.b)

    def div(self):
        print('Div is :',self.a/self.b)

cal = Calculator()
cal.sum()
cal.diff()
cal.Mul()
cal.div()