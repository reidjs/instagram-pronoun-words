import itertools
import sys

words = open("words_alpha.txt", encoding="utf8").readlines()
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
            sys.stdout.write(joined_word)
            sys.stdout.write("\n")