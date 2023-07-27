# Practice with files and dictionaries.
# Count the numer of letter grades using a dictionary.
# Thomas D'Angelo

letters = ["A", "B", "C", "D", "F"]
counts = {}

file = "letter_grades.txt"

# Loop through all lines in the file.
for line in open(file):
    letter = line.replace("\n", "") # Strip \n, assign to letter
    count = counts.get(letter, 0)   # Get the count of the letter if it exists
    counts[letter] = count + 1      # Store count

for l in letters:
    print(l + ":", counts.get(l, 0))