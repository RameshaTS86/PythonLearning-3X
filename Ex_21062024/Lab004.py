#decorator - is function which takes another function as input


def my_decor(func):

    def wrapper():
        print('Strating......')
        print('**************')
        func()
        print('**************')
        print('Ending......')

    return wrapper()


@my_decor
def say_hello():
    print('Hello, Good Morning.!')