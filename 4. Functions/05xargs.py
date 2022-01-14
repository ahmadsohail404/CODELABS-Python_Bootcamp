# **args

def multiply(*numbers):
    # print(numbers)  # o/p -> (2, 3, 4, 5) called tuples it's iterable i.e we can loop
    # [2,3,4,5] -> this is called list
    total = 1
    for number in numbers:
        # total *= number
        total = total * number
    return total


print(multiply(2, 3, 4, 5))
