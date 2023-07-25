# This is just a test of each of the different problems in the worksheet.

def func_a():
    j = 4                           # Loop variable
    while j > -4:
        print(j)
        j -= 1


def func_b():
    string = "Hello"
    builder = ""                    # Accumulator
    i = 0
    while i < len(string):
        builder += string[i].swapcase()
        print(i, builder)
        i += 1
    print(string, "->", builder)


def func_c():
    x = 0
    i = 1
    while x < 20:
        if x > 5:
            x += 15
        else:
            x += 1
        print(i, x)
        i += 1


def func_2a():
    string = "HELLO"
    x = 0
    while string[x] != 'L':
        print(string[x], end="... ")
        x += 1
    print("\n", string, "first L is at", x)


def func_2b():
    # Assume the user enters the following:
    # hellow goodbye cat dog DONE done
    list = []
    prompt = "Please enter word, 'done' to finish "
    response = input(prompt)
    while response != "done":
        list.append(response)
        response = input(prompt)
    print(sorted(list))


def func_2c():
    x = 0
    while x < 20:
        if x > 5:
            if x % 2 == 0:
                x *= 2
            else:
                x *= -1
        else:
            x += 10
        x += 1
    print(x)


# Testing each function
def main():
    print("--------------- ")
    print("Running func_a ")
    func_a()

    print("--------------- ")
    print("Running func_b ")
    func_b()

    print("--------------- ")
    print("Running func_c ")
    func_c()

    print("--------------- ")
    print("Running func_2a ")
    func_2a()

    print("--------------- ")
    print("Running func_2b ")
    func_2b()

    print("--------------- ")
    print("Running func_2c ")
    func_2c()


main()
