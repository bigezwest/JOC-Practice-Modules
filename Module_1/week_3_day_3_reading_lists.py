#reading_lists.py
#Thomas D'Angelo
# What does this program output?

my_list = ["one", "two", "three", "four", "five"]
print("\t------------------------------------------------------")
print("\tTEST 1")
print("\n\tTrue indicates that the result is what was expected")
print("\tTest\t\t\t Result")
print("\t----------\t\t -----------")
print("\tmy_list[0]\t\t", my_list[0] == "one")
print("\tmy_list[-1]\t\t", my_list[-1] == "five")
print("\tmy_list[2:4]\t", my_list[2:4] == ["three", "four"])
print("\t------------------------------------------------------")

print("\n\tTEST 2")
print("\t-------")
for num in my_list:
    if num.count("o") > 0:
        print("\t", num)

print("\t------------------------------------------------------")

print("\n\tTEST 3")
print("\t______")
phrase = "Green Eggs & Ham"
print(("green" in phrase) == False)
print(("Green" in phrase) == True)
print(("two" in phrase) == False)

print("\t------------------------------------------------------")
print("\tTEST 4")
phrase = "Monty Python"
for letter in phrase:
    print(letter, end="-")
print()

print("\t------------------------------------------------------")
print("\tTEST 1")
# Assume ythe user enters the following numbers:
# 5 10 15 20 25
numbers = []
for i in range(5):
    numbers.append(int(input("Please enter a number: ")))
print(sum(numbers))