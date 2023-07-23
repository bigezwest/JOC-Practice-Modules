# writing_lists_1.py
# Thomas D'Angelo
#
# 1. Write a program that creates a list of 20 numbers input by the user and prints
# the average (mean) of the list.


# Create a list of 20 numbers, input by user.
def writeAList():
    my_list = []
    for i in range(20):
        user_num = int(input("Enter a number: "))
        my_list.append(user_num)

    total = 0                       # Accumulator for total
    length = 0                      # To hold the size of the list
    for item in (my_list):
        total += item               # Add to total
        length += 1                 # Increment length of list
    avg = total / length            # Calculate the average
    print("The average of the numbers is", avg)

def main():
    writeAList()


main()
