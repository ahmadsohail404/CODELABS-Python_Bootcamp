def fizz_buzz(input):
    if (input % 3 == 0) and (input % 5 == 0):  # more specific condition on top
        return "FizzBuzz"
    elif input % 3 == 0:
        return "Fizz"
    elif input % 5 == 0:
        return "Buzz"
    return input


print(fizz_buzz(15))
