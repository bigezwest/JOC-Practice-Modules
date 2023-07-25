# Write python code to print the following using while loops:
# a.
#   1
#   2
#   3
#   4
#   5

def to_5(num):
    while num <= 5:
        print(num)
        num += 1


# b.
#   2
#   5
#   8
#   11
def by_3s(num):
    while num <= 11:
        print(num)
        num += 3


# c. -10 -8 -6 -4 -2 0
def by_2s(num):
    while num <= 0:
        print(num, end=" ")
        num += 2


# d.
#   ****
#   ****
#   ****
#   ****
def print_stars(ch, count):
    i = 0
    while i < count:
        print(ch * count)
        i += 1


# 2. Write a while loop that prints the letters in “CSCI 150” on separate lines.
def show_course(course):
    i = 0
    while (i < len(course)):
        print(course[i])
        i += 1


# 3.
# Create a program that allows the user to enter in a list of numbers, prints them out in sorted order,
# and prints the sum and average of the numbers. Prompt the user to continue entering numbers,
# and enter the number ‘0’ when finished.
def list_work():
    user_list = []
    user_ans = 1
    while user_ans != 0:
        user_ans = int(input('Enter a number or 0 to quit: '))
        if user_ans != 0:
            user_list.append(user_ans)

    print()
    print("User List:", sorted(user_list))
    print("Sum of Nums:", sum(user_list))
    print("Average of Nums:", (sum(user_list)/ len(user_list)))
def main():
    print('Running to_5.  Prints to 1 - 5.')
    to_5(1)
    print('-------------------------------- ')

    print('Running by_3s.  Increments by 3 and prints. ')
    by_3s(2)
    print('-------------------------------- ')

    print('Running by_2s.  Increments by 2 and prints')
    by_2s(-10)
    print()
    print('-------------------------------- ')

    print('Running print_stars.  Prints a char, count times.')
    print_stars("*", 4)
    print('-------------------------------- ')

    print('Running show_course("CSCI 150")')
    show_course("CSCI 150")
    print('-------------------------------- ')

    print('Running list_work()')
    list_work()
    print('-------------------------------- ')

main()
