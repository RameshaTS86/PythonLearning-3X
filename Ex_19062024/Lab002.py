#nesteed Functions

def My_fun1():
    print('Outer Function')
    def My_inner_fun1():
        print('I am Inner Function')
    My_inner_fun1()

My_fun1()