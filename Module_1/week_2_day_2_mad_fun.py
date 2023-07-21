# Take a float input and output function results
import math

user_float = float(input("Enter a decimal number: "))
print("\t------------------------------")
print("\tThe absolute value is", abs(user_float))
print("\tThe number rounded is", round(user_float, 0))
print("\tThe square root is", math.sqrt(abs(user_float)))
print("------------------------------")