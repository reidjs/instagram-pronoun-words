import itertools
import sys

found = []

output = open('out.txt', 'w')
words = open("words_alpha.txt").readlines()
dictionary = {}
for word in words:
    w = word.strip()
    dictionary[w] = True

raw_pronouns = open("pronouns.txt").readlines()
pronouns = []
for pronoun in raw_pronouns:
    p = pronoun.strip()
    pronouns.append(p)

for L in range(1, 4):
    for subset in itertools.combinations(pronouns, L):
        joined_word = "".join(subset)
        lookup = dictionary.get(joined_word)
        if (lookup):
            found.append(joined_word + ": " + subset.__str__() + "\n") # This is optional but it shows the subsets used to create the word!

found = [*set(found)] # Removes Duplicates
found.sort() # Alphabetizes
for toWrite in found:
    sys.stdout.write(toWrite)
