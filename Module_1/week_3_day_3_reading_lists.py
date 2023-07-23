#reading_lists.py
#Thomas D'Angelo
# What does this program output?

my_list = ["one", "two", "three", "four", "five"]
print("------------------------------------------------------")
print("TEST 1")
print("\nTrue indicates that the result is what was expected")
print("Test\t\t\t Result")
print("----------\t\t -----------")
print("my_list[0]\t\t", my_list[0] == "one")
print("my_list[-1]\t\t", my_list[-1] == "five")
print("my_list[2:4]\t", my_list[2:4] == ["three", "four"])
print("------------------------------------------------------")

print("\nTEST 2")
print("-------")
for num in my_list:
    if num.count("o") > 0:
        print(num)

print("------------------------------------------------------")

print("\nTEST 3")
print("______")
phrase = "Green Eggs & Ham"
print(("green" in phrase) == False)
print(("Green" in phrase) == True)
print(("two" in phrase) == False)

print("------------------------------------------------------")
print("\nTEST 4")
print("______")

phrase = "Monty Python"
for letter in phrase:
    print(letter, end="-")
print()

print("------------------------------------------------------")
print("\nTEST 5")
print("______")

# Assume ythe user enters the following numbers:
# 5 10 15 20 25
numbers = []
for i in range(5):
    numbers.append(int(input("Please enter a number: ")))
print(sum(numbers))