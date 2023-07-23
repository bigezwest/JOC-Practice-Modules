# are_we.py
# Thomas D'Angelo
#
# 8. Write a function are_we that takes a number of times to repeat and a phrase to
# be repeated as parameters and outputs the following for the given calls:
# Example call Prints:
#   are_we(2, “there”) Are we there yet? Are we there yet?
#   are_we(3, “50”) Are we 50 yet? Are we 50 yet? Are we 50 yet?
#   are_we(1, “”) Are we yet?
#   are_we(0, “hey!”)

def are_we(num, phrase):
    return ("Are we " + phrase + " yet? ") * num


def main():
    print("\t------------------------------------------------- ")
    print("\tTest\t\t\t\t\t\t\t Results of tests:")
    print("\t----\t\t\t\t\t\t\t ----------------")
    print('\tResult of: are_we(2, "there"):\t', are_we(2, "there"))
    print('\tResult of: are we(3, "50"):\t\t', are_we(3, "50"))
    print('\tResult of: are we(1, ""):\t\t', are_we(1, ""))
    print('\tResult of: are we(0, "hey!"):\t', are_we(0, "hey!\n"))
    print("\t------------------------------------------------- ")


main()
