# Write a function, pyramid, that takes a single character and a number as parameters and displays an
# ASCII art pyramid to the screen with number rows:


def pyramid(char, size):
    for i in range(size):
        print(char * (i + 1))
    print()


def main():

    print('Running: pyramid("*", 2)')
    pyramid("*", 2)

    print('Running: pyramid("+", 5)')
    pyramid("+", 5)

    print('Running: pyramid("x", 10)')
    pyramid("x", 10)


main()
