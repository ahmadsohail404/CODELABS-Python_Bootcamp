# when we work with files, network connections, databases and so on,
# after using these resources we release them i.e we open a file which always
# closes when it's done

try:
    file = open("04cleaning_up.py")
    age = int(input("Age: "))
    xfactor = 10/age            # it'll crash at age = 0 -> ZeroDivisionError
except (ValueError, ZeroDivisionError) as ex:
    print("You didn't enter a valid age 🥲")
else:
    print("No exceptions found!")
finally:    # this clause always executes
    file.close()
