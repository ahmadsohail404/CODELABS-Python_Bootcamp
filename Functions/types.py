# 1. Perform a task
# 1. Return a value

# all functions returns none by default
def greet(name):
    print(f"Hello {name}!")


greet("Meow")


def get_greeting(name):
    return f"Hello {name}!"


message = get_greeting("This is the content of the content.txt file")
print(message)

file = open("content.txt", "w")   # creates a file and puts the value in it.
file.write(message)
