def logging_decorator(function):
    def wrapper(*args):

        print(f"You called {function.__name__}{args}")
        result = function(args[0], args[1], args[2])
        print(f"It returned {result}")
    return wrapper


@logging_decorator
def add_function(a: int, b: int, c: int):
    return a + b + c


add_function(1, 2, 3)
