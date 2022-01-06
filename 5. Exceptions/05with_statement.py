# exception handling without the final clause
# the with statement is used to automatically release external resources.

try:
    with open("04cleaning_up.py") as file, open("01exception.py") as target:
        print("File opened.")
        # file.__enter__                # -> magic methods
        # file.__exit__             # reason for not using final clause
    age = int(input("Age: "))
    xfactor = 10/age
except (ValueError, ZeroDivisionError) as ex:
    print("You didn't enter a valid age 🥲")
else:
    print("No exceptions found!")
