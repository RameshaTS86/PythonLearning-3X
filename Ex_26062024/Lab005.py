class Calculator:

    def __init__(self,a,b):
        self.a = a
        self.b = b
    def sum(self):
        print('Sum is :',self.a+self.b)

    def diff(self):
        print('Diff is :',self.a-self.b)

    def Mul(self):
        print('Mul is :',self.a*self.b)

    def div(self):
        print('Div is :',self.a/self.b)

Calculator(10,10).sum()
Calculator(10,10).diff()
Calculator(10,10).Mul()
Calculator(10,10).div()