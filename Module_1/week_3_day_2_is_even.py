# Writing is_even
# Thomas D'Angelo
#
# Write a function is_even that takes a number as a parameter and returns whether or not it is even.
# Test that your function works by calling it twice, once with an even number and once with an odd
# number, and print the results.

# Tests if a number is even.  Boolean return
def is_even(num):
    return num % 2 == 0


def main():
    print("4 is even?", is_even(6))
    print("3 is even?", is_even(3))


main()
