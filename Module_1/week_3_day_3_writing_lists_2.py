# writing_lists_2.py
# Thomas D'Angelo
#
# 2. Write a function mangle that takes a string as a parameter and returns the string after performing
# the following operations:
#   i. Converting the string to all upper case letters
#   ii. Removing the third character
#   iii. Removing the third to last character
# Test that your function works.
# Hint: Think about how you can remove from a string by creating a new string, adding characters to it,
# and omitting the characters you don’t want?
#   Example function calls: Output:
#       print(mangle(“hellothere”)) HELOTHRE
#       print(mangle(“42 degrees Celsius”)) 42DEGREES CELSUS
#       print(mangle(“eeeeeee”)) EEEEE

def mangle(string):
    string = string.upper()
    string = string[0:2] + string[3:-3] + string[-2:]
    return string

def main():
    test_input = ["hellothere", "42 degrees Celsius", "eeeeeee"]
    test_output = ["HELOTHRE", "42DEGREES CELSUS", "EEEEE"]
    for i in range(len(test_input)):
        print("Mangle", test_input[i] + ":", mangle(test_input[i]) == test_output[i])


main()
