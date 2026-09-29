# decorator means way of decorate a things in simple way like -> function call, time 

from functools import wraps

def my_decorators(func):
    @wraps(func)
    def wrapper():
        print("something before function")
        func()
        print("something after function")
    return wrapper

@my_decorators
def say_chai():
    print("chai is ready !")

say_chai()
print(say_chai.__name__)