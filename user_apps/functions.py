import re
import random


def mix_middle_chars(text):
    words = re.split('(\W)', text)
    scrambled_words = []

    for word in words:
        if len(word) <= 3 or word in (' ', '\n'):
            scrambled_words.append(word)

        else:
            # Extract first, middle, and last parts of the word
            first_letter = word[0]
            middle_letters = list(word[1:-1])
            last_letter = word[-1]

            # Shuffle the middle letters
            random.shuffle(middle_letters)

            # Join the first, shuffled middle, and last letters together
            scrambled_word = first_letter + ''.join(middle_letters) + last_letter
            scrambled_words.append(scrambled_word)

    return ''.join(scrambled_words)
