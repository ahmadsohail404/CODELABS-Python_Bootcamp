# everything in python is an object, here course is an object
course = "  Python Programming"

# we can access the methods using dot notation
print(course.upper())
print(course)           # the original string is not affected

print(course.strip())   # the white spaces will be removed
# rstrip() -> right strip, lstrip() -> left strip

print(course.find("Pro"))  # returns index of Pro

print(course.replace("P", "J"))

print("Pro" in course)      # returns boolean
print("swift" not in course)      # returns boolean
