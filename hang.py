import random
import string

from valid_words import val_words
from hang_visual import hang_visual_dict


# -------------Function that will randomly choose a word from the list

def get_vword(val_words):
    word = random.choice(val_words)

    while '-' in word or ' ' in word:
        word = random.choice(val_words)

    return word.upper()


def hang():
    word = get_vword(val_words)
    w_letters = set(word)  # ----- letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # ------- letters guessed

    lives = 10

    # -------------- User Input

    while len(w_letters) > 0 and lives > 0:
        # -------- Letters guessed and Lives left
        print('You have', lives, 'lives left, \nYou have used the following letters: ', ' '.join(used_letters))

        # ------- what current word is (ex: W - R D)
        word_ls = [letter if letter in used_letters else '-' for letter in word]
        print(hang_visual_dict[lives])
        print('Current word: ', ' '.join(word_ls))

        user_guess = input('Guess a letter: ').upper()
        # ------------ Condition that places the users guess among the other previously guessed letters
        if user_guess in alphabet - used_letters:
            used_letters.add(user_guess)

    # ------------ indicates a user has guessed a letter in the word correctly and removes the letter from the word
            if user_guess in w_letters:
                w_letters.remove(user_guess)
                print('')

            else:
                # ----------- Subtracts a Life When an Incorrect Guess is Made
                lives = lives - 1
                print('The letter,', user_guess, 'is not in this word')

        elif user_guess in used_letters:
            print('You have already guessed that character, try again.')

        else:
            print('Invalid character, try again.')

    # --------- When the word has been guessed or lives == 0
    if lives == 0:
        print(hang_visual_dict[lives])
        print("Game Over, you died. The correct word was", word)
    else:
        print('Congratulations! The word was', word, '🐙')


if __name__ == '__main__':
    hang()
