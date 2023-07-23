# 7. Write a function, there, that takes a number n as a parameter, and returns 2n if n is positive, and 0 otherwise.
# Your function should output the following for the given calls:
# Example call Returns:
#       there(5) 32
#       there(0) 1
#       there(3) 8
#       there(-2) 0
#       there(-6) 0

# Returns 2 raised to n power if n > 0.  else returns 0
def there(n):
    if n >= 0:
        return 2 ** n
    else:
        return 0


# Testing there()
def main():
    print("\n\tTest Results")
    print("\t------------------------------ \t")
    print("\t2 raised to the 5th power is: \t", there(5))
    print("\t2 raised to the 0 power is: \t", there(0))
    print("\t2 raised to the 3rd power is: \t", there(3))
    print("\t2 raised to the -2nd power is: \t", there(-2))
    print("\t2 raised to the -6th power is: \t", there(-6))


main()