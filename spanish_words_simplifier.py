def remove_accents(word):
    accents = {'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u', 'ü': 'u', 'ñ': 'n'}
    for accented_char, unaccented_char in accents.items():
        word = word.replace(accented_char, unaccented_char)
    return word

def simplify(word_list):
    simplified_words = []
    for word in word_list:
        simplified = remove_accents(word)
        simplified_words.append(simplified)
    return simplified_words