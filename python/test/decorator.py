# -*-coding:utf-8-*-

from functools import wraps

def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("%s was called" % func.__name__)
        func(*args, **kwargs)
        
    return wrapper

@decorator
def testDecorator(name="decorator"):
    print("this is %s!" % name)

print(testDecorator.__name__)
testDecorator('testDecorator')