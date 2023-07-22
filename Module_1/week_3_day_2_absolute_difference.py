# Thomas D'Angelo
# Write a function, absolute_difference, that takes two numbers as parameters and returns
# their absolute difference.

# Return the absolute difference of 2 numbers
def absolute_difference(x, y):
    return abs(x - y)


def main():
    print(absolute_difference(5, 10))           # Test with negative difference
    print(absolute_difference(10, 5))           # Test with positive difference
    print(absolute_difference(200, -200))       # Test subtracting a negative.  (adding)


main()
