# Originally print() -> print("something", \n), here \n is by default in print().

print("Python", end=" ")  # Python3 end parameter in print()
print("Bootcamp")
# ends the output with a <space>

print("Python", end='@')
print("NISB")

# array
a = [1, 2, 3, 4]

for i in range(4):
    print(a[i], end=" ")
print()
print()

# without using loop
b = [5, 6, 7, 8]
print(*b)
