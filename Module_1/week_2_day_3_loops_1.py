# Writing Loops
# Thomas D'Angelo
# 1a
for i in range(1, 6):
    print(i)
# 1b
print("--------")
for i in range(2, 12, 3):
    print(i)
# 1c
print("--------")
for i in range(-10, 1, 2):
    print(i, end=" ")
# 1d
print("\n--------")
for i in range(4):
    print("*" * 4)

print("\n--------")
for i in range(4):
    for j in range(4):
        print('*', end="")
    print()
# 2
print("--------")
word = "CSCI 150"
for letter in word:
    print(letter)
# 3
print("--------")
for i in range(1, 11):
    print(i)
    