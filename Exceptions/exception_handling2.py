try:
    age = int(input("Age: "))
    xfactor = 10/age            # it'll crash at age = 0 -> ZeroDivisionError
except (ValueError, ZeroDivisionError) as ex:
    print("You didn't enter a valid age 🥲")
# except ZeroDivisionError:
#     print("Age cannot be zero 😂")
else:
    print("No exceptions found!")
