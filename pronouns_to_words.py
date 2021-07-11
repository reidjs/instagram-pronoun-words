import itertools
import sys

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

ig_words = {}
for L in range(0, len(pronouns) + 1):
    for subset in itertools.combinations(pronouns, L):
        for M in range(1, len(subset) + 1):
            for subset2 in itertools.combinations(subset, M):
                joined_word = "".join(subset2)
                lookup = dictionary.get(joined_word)
                # NOTE: unfortunately this algorithm generates a lots of duplicates
                already_exists = ig_words.get(joined_word)
                if (lookup and not already_exists):
                    ig_words[joined_word] = True
                    sys.stdout.write(joined_word)

