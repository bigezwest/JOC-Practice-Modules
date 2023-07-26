# 1. Write a function average_neg_evens that takes a list of numbers as a parameter,
# and adds all the negative even numbers (less than 0 and divisible by 2) together and returns their average.
#   Example function call:
#       print(average_neg_evens([0, 1, 2, -2, -3, -4, 3, 4]))
#       Outputs: -3

def average_neg_evens(user_list):
    temp_list = []                              # To hold values that fit criteria in line 13
    for num in user_list:                       # for each value in the list
        if num < 0 and num % 2 == 0:            # find the number that fit criteria
            temp_list.append(num)               # add that number to the temp list
    print("The negative, even numbers are", temp_list)
    return sum(temp_list) / len(temp_list)      # return the average


# 2. Write a function count_letter that takes a list of strings and a string letter as parameters and returns
# the number of times this letter occurs, both upper- & lower-cased.
#   Example function call:
#       list = [“HELLO”, “goodbye”, “1234 Oooh!”]
#       print(count_letter(list, “o”))
#       Outputs: 6
def count_letter(user_list, ch):
    ch = ch.lower()                     # to hold char to search for.  make it lowercase
    count = 0                           # count of occurrences

    i = 0
    while i < len(user_list):
        for word in user_list:                  # for each word in list
            for word_char in word:              # for each char in that word
                if word_char.lower() == ch:     # if char.lower == searched for char
                    count += 1                  # add one to count
                i += 1
    return count


def main():
    a_list = [0, 1, 2, -2, -3, -4, 3, 4]
    print("THe input list is: ", a_list)
    print("The average of the negative, even numbers is: ", average_neg_evens(a_list))
    print("---------------------------------------------------- ")

    ch = "o"
    b_list = ["HELLO", "goodbye", "1234 Oooh!"]
    print("The input list is", b_list)
    print('Searching for ', ch)
    print("There are", count_letter(b_list, ch), "occurrences of", ch)


main()
