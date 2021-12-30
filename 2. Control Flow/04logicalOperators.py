# and
# or
# not

high_income = True
good_credits = False
student = True

message = "Eligible" if high_income and good_credits else "Not eligible"
print(message)

message = "Eligible" if high_income or good_credits else "Not eligible"
print(message)

message = "Eligible" if not student else "Not eligible"
print(message)

message = "Eligible" if (
    high_income or good_credits) and not student else "Not eligible"
print(message)
