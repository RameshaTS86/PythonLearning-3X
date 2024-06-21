#Decorator real time example

import time

def time_decor(func):

    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        print('Time Taken is : ', round(end_time - start_time,2))

    return wrapper()


@time_decor
def mylogs():
    time.sleep(5)
    print('This is my logs')

@time_decor
def mylogs2():
    time.sleep(10)
    print('This is my logs 2')
