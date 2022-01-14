def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total   # knowingly writing along in indentation for debugging


print("start")
print(multiply(2, 3, 4))
