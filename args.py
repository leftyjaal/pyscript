def function(*args):
    total = 0
    for i in args:
        total += i
    return total

def more_args(**kwargs):
    print(kwargs)

def fruit_values(**kwargs):
    total = 0 
    for value in kwargs.values():
        total += value

    return total

# print(function(10, 10, 20, 5))

# more_args(banana=10, mango=5, apple=1)

print(fruit_values(banana=5, mango=7, apple=3, orange=10))

