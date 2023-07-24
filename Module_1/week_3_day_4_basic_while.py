# This is just a test of each of the different problems in the worksheet.

def func_a():
    j = 4
    while j > -4:
        print(j)
        j -= 1


def func_b():
    string = "Hello"
    builder = ""
    i = 0
    while i < len(string):
        builder += string[i].swapcase()
        print(i, builder)
        i += 1
    print(string, "->", builder)


# Testing each function
def main():
    print("--------------- ")
    print("Running func_a ")
    func_a()

    print("--------------- ")
    print("Running func_b ")
    func_b()



main()
