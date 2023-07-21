# Ask the user for 2 parts of speech as input.  Output a simple poem.

user_noun = input('Enter a plural noun: ')
user_adj = input('Enter an adjective: ')

user_noun = user_noun.capitalize()
user_adj = user_adj.lower()

print(user_noun, "are red, violets are blue")
print("Month Python is", user_adj + ", woo hoo!")
