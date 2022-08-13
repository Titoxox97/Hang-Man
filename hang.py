import random
from valid_words import val_words

# -------------Function that will randomly choose a word from the list

def get_vword(val_words):
    word = random.choice(val_words)

    while '-' in word or ' ' in word:
        word = random.choice(val_words)

    return word

