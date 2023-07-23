# hey
# Thomas D'Angelo
#
# 6. Write a function hey that takes a number as a parameter, squares it, and outputs the parameter squared:
# Example call Returns
#   hey(5) 25
#   hey(0) 0
#   hey(-3) 9

# Return the square of a number
def hey(num_1):
    return num_1 ** 2


# Calls and prints hey() to show the square of number
def main():
    print('\t---------------------------------------------------')
    print('\tTest\t\t\t\t\t Function Call\t\t Result')
    print('\t----\t\t\t\t\t -------------\t\t ------')
    print("\tPostive Number Test:\t Calling hey(5)\t\t", hey(5) == 25)      # Positive test
    print("\tZero Test:\t\t\t\t Calling hey(0)\t\t", hey(0) == 0)           # 0 test
    print("\tNegative Number Test:\t Calling hey(-3)\t", hey(-3) == 9)      # Negative test
    print('\t---------------------------------------------------')

main()
