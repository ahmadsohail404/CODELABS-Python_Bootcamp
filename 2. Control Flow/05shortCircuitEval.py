high_income = False
good_credits = True
student = True

if high_income and good_credits and not student:
    # the python interpreter starts evaluation from start,
    # wherever it find false then it stops there
    # because it knows further evaluation is useless and result is judged there only
    print("Eligible")

if high_income or good_credits or not student:
    # the evaluation stops as soon as we find true
    print("Eligible")
