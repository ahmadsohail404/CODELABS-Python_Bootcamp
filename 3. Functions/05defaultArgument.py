def increment(number, by=1):  # we can't add another parameter after by=1
    # optional paramenter should come after the required parameter.
    return by + number


print(increment(2, 5))
