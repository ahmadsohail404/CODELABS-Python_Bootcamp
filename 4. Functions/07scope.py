message = "a"   # global variable -> scope is this whole file


# here name and message are local variables having scope as their functions
def send_email(name):
    message = "a"

# print(name)  # it has no idea what name is


def greet(name):
    global message  # but bad practise
    message = "b"


greet("Sohail")  # interpreter will allocate memory for name and message at execution
print(message)
