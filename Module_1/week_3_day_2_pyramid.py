# Write a function, pyramid, that takes a single character and a number as parameters and displays an
# ASCII art pyramid to the screen with number rows:


def pyramid(char, size):
    for i in range(size):
        print(char * (i + 1))
    print()


def main():

    pyramid("*", 2)
    pyramid("+", 5)
    pyramid("x", 10)


main()
