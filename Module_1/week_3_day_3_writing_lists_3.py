# 3. Write a function, count_e, that takes a list of strings as a parameter and returns the total number
# of upper and lower case e’s (“E” and “e”) in all the strings in the list.
# Test that your function works with multiple examples.
#   Example function call:                          Output:
#       print(count_e([“hi”, “hello”, “EEK!”]))     3

def count_e(strings):
    total = 0
    for word in strings:
        total += word.upper().count("E")
    return total


def main():
    string_list = ["hi", "hello", "EEK!"]
    print(count_e(string_list))


main()
