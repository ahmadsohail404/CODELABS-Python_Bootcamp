arr = []

n = int(input("Enter number of students: "))
for i in range(n):
    ele = str(input(f"Enter student {i+1} name: "))
    arr.append(ele)

print("List of students' name: ", arr)
