# What does this program output when it's ....
# 1. Monday?
# 2. Saturday
# 3. Sunday
# 4. Raining
#
DoW = input("What day is it? ").title()
# DoW = DoW.title()

if DoW == "Saturday":
    print("Wake up at 9 am")
elif DoW == "Sunday":
    print("Wake up at 10 am")
else:
    print("Wake up at 7 am")

