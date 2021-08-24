def add(*args):
    total = sum([num for num in args])
    return total

print(add(1, 2, 3, 4, 5))

def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    return n

print(calculate(2, add=3, multiply=100))


class Car:
    def __init__(self, **kwargs):
        # kwargs.get() returns None if value is missing
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.seats = kwargs.get("seats")

my_car = Car(make="BMW", model="i3")
print(my_car.model)