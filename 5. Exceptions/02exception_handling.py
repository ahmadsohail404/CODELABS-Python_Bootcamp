try:
    age = int(input("Age: "))
except ValueError as ex:           # called exception clause
    print("You didn't enter a valid age 🥲")
    # print(ex)
    # print(type(ex))
else:
    print("No exceptions found!")

print("Execution continues...")
