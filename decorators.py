def f1(func):
    def wrapper(*args, **kwargs):
        print("Started")
        val = func(*args, **kwargs)
        print("Ended")
        return val
    return wrapper


@f1
def f(a, b=9):
    print(a, b)


@f1
def add(x, y):
    print("Inside add function")
    return x + y


print(add(4, 5))
