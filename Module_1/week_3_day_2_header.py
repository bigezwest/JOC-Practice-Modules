"""
Thomas D'Angelo

"""


def header(text, surround_char):
    length = len(text) + 4

    print(surround_char * length)
    print(surround_char, text, surround_char)
    print(surround_char * length)


def main():
    my_surround_char = "*"
    my_text = "Hello, World"

    header(my_text, my_surround_char)
    header("Python Rocks", "!")
    header("Coders 4 EVER", "+")


main()
