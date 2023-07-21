# Writing Loops 2
# by Thomas D'Angelo
#
# This program calculates and prints the average of 10 real numbers, entered by the user.
#   - req - Make sure you ask the user to enter each number (the user will hit enter after each number).

print('This program will ask you for 10 numbers.')
print('After entering the numbers, you will get back an average.')
user_range = 10
user_total = 0

for i in range(user_range):
    user_total += float(input("Enter a real number: "))

print('Your average is', user_total / user_range)
