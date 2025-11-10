import itertools
import sys
import spanish_words_simplifier

spanish_word_list = open("words_spanish.txt", encoding="utf8").readlines()
words = spanish_words_simplifier.simplify(spanish_word_list)

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