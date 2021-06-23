def greet(target, *args, **kwargs):
    print("Hello world!", args, kwargs)


a = True
b = 0.123


def f1(func):
    def f2():
        print("f2 started")
        val = func()
        print("f2 finished")
        return val
    return f2


greet('This is a string', a, b, f1, key=12)
