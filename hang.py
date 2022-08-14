import random
import string

from valid_words import val_words

# -------------Function that will randomly choose a word from the list

def get_vword(val_words):
    word = random.choice(val_words)

    while '-' in word or ' ' in word:
        word = random.choice(val_words)

    return word


def hang():
    word = get_vword(val_words)
    w_letters = set(word)   # ----- letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # ------- letters guessed

    # -------------- User Input

    user_guess = input('Guess a letter: ').upper()
    # ------------ Condition that places the users guess among the other previously guessed letters
    if user_guess in alphabet - used_letters:
        used_letters.add(user_guess)
    # ------------ indicates a user has guessed a letter in the word correctly and removes the letter from the word
        if user_guess in w_letters:
            w_letters.remove(user_guess)

    elif user_guess in used_letters:
        print('You have already guessed that character, try again.')

    else:
        print('Invalid Character')