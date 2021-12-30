# def increment(number, by):
#     return by + number


# value = increment(2, 1)
# print(value)

# use this👇🏻
def increment(number, by):
    return by + number


print(increment(2, by=1))   # more readable
# the python interpreter first calls the function and stores the result temporarily
# in a variable we don't see and then it'll pass that variable as an argument to the
# print function
