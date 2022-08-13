import random
from valid_words import val_words

# -------------Function that will randomly choose a word from the list

def get_vword(valid_words):
    valid_words = random.choice(valid_words)