"""
Thomas D'Angelo
    1. Write a function, add, that takes two numbers as parameters and returns their sum.
    2. Write a function, multiply, that takes two numbers as parameters and returns their product.
    3. Now, test! Write python code that gets two numbers as input from the user and prints out their sum and product
         by calling the two functions above. Bonus points for putting this part in a main function.
"""


# Adds 2 numbers, returns sum
def add(num_1, num_2):
    return num_1 + num_2


# multiplies 2 numbers, returns result
def multiply(num_1, num_2):
    return num_1 * num_2


# Get 2 user nums, add and multiply, display results
def main():
    print("----------------------------------------")
    print("This program will ask you for 2 numbers ")
    print("and return their sum and product. \n")
    user_num_1 = int(input("\tEnter a number: "))
    user_num_2 = int(input("\tEnter another number: "))
    print()
    print("The sum of ", user_num_1, " and ", user_num_2, " is ", add(user_num_1, user_num_2), ". ", sep="")
    print("The product of ", user_num_1, " and ", user_num_2, " is ", multiply(user_num_1, user_num_2), ". ", sep="")
    print("----------------------------------------")

main()
