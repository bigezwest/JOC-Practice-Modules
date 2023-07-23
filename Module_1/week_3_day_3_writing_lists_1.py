# writing_lists_1.py
# Thomas D'Angelo
#
# 1. Write a program that creates a list of 20 numbers input by the user and prints
# the average (mean) of the list.


# Create a list of 20 numbers, input by user.
def writeAList():
    list = []
    for i in range(20):
        user_num = int(input("Enter a number: "))
        list.append(user_num)
    print("Average: ", sum(list) / len(list))

def main():
    writeAList()


main()
