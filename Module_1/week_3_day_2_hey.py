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
    print("5 squared is ", hey(5))      # Positive test
    print("0 squared is", hey(0))       # 0 test
    print("-3 squared is", hey(-3))     # Negative test


main()
