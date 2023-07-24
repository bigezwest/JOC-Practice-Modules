# 4. Write a function, count_vowels, that takes a list of strings as a parameter and returns the
# total number of upper and lower case vowels (A, E, I, O, U) in all the strings in the list.
#   Example function call:                                  Output:
#       print(count_vowels([“hi”, “hello”, “OOF!”]))        5

def count_vowels(word_list):
    vowel_list = ["a", "e", "i", "o", "u"]
    count = 0                                       # Aggregator for vowels

    for letter in vowel_list:                       # For each letter in the vowel list
        for word in word_list:                      # for each word in the word list
            count += word.count(letter) or \
                     word.count(letter.upper())     # Add one for an upper or lowercase vowel
    return count


def main():
    word_list = ["hi", "hello", "OOF!"]
    word_list_2 = ["This", "is", "another", "test", "buffalo"]

    print("Word List 1: ", count_vowels(word_list))
    print("Word List 2: ", count_vowels(word_list_2))


main()
