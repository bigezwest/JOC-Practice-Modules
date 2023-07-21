# Writing Loop Word Problems
# Thomas D'Angelo

# 1
for i in range(10, 26, 5):
    print(i, end=" ")
print()

# 2
print("------------------\n")
for i in range(-3, 22, 3):
    if i < 21:
        print(i, ",", end=" ", sep='')
    else:
        print(i, end=" ", sep='')
print()

''' Alternative Solution
print("------------------\n")
for i in range(-3, 21, 3):
    print(i, end=", ")
print(i + 3)
'''
# 3
# See avg.py
print("------------------\n")
print("See week_2_day_3_avg.py for question 3.")

