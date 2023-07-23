# Write a function is_even that takes a number as a parameter and returns whether or not it is even.
# Test that your function works by calling it twice, once with an even number and once with an odd
# number, and print the results.

def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False


def main():
    print (is_even(6))
    print(is_even(3))


main()
