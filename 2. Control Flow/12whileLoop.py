# 1. Single statement while block
count = 0
while (count == 0):
    print("Hello Geek")

# 2.
count = 0
while (count < 3):
    count = count + 1
    print("Hello Geek")
else:
    print("In Else Block")

# 3.
number = 100
while number > 0:
    print(number)
    number //= 2


# 4. printing input till quit
command = ""
while command.lower() != "quit":
    command = input(">")
    print("ECHO", command)
