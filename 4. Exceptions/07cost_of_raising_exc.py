from timeit import timeit

code1 = """
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less.")
    return 10/age


try:
    calculate_xfactor(-1)
except ValueError as error:
    pass #using it here because we can't leave the clause empty
"""

code2 = """
def calculate_xfactor(age):
    if age <= 0:
        return None
    return 10/age


x_factor = calculate_xfactor(-1)
if x_factor == None:
    pass

"""
# do it again
print("first code: ", timeit(code1, number=10000))
print("second code: ", timeit(code2, number=10000))
