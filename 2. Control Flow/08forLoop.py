for number in range(1, 10, 2):
    print(number, "Attempt", (number) * "*")  # no need to write number+1
# The third argument is the incremented value

# 1 Attempt *
# 3 Attempt ***
# 5 Attempt *****
# 7 Attempt *******
# 9 Attempt *********


# Iterating over a list (mutable)
print("List Iteration")
list = ["python", "is", "awesome"]
for i in list:
    print(i)

# Iterating over a tuple (immutable)
# This means that tuples cannot be changed while the lists can be modified.
print("\nTuple Iteration")
t = ["python", "is", "awesome"]
for i in t:
    print(i)

# Iterating over a String
print("\nString Iteration")
s = "Engineering"
for i in s:
    print(i)
