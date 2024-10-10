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


def verify_pesel_data(pesel):
    if len(pesel) == 11:

        # Get first two digits of the year and month
        if pesel[2] in ('8', '9'):
            year = '18'
            month = int(pesel[2:4]) - 80
        elif pesel[2] in ('0', '1'):
            year = '19'
            month = pesel[2:4]
        elif pesel[2] in ('2', '3'):
            year = '20'
            month = int(pesel[2:4]) - 20
        elif pesel[2] in ('4', '5'):
            year = '21'
            month = int(pesel[2:4]) - 40
        elif pesel[2] in ('6', '7'):
            year = '22'
            month = int(pesel[2:4]) - 60
        # Concat full year
        year = year + pesel[:2]

        # Get gender
        if int(pesel[9]) % 2 == 0:
            gender = 'kobieta'
        else:
            gender = 'mężczyzna'

        # Control sum
        weights = (1, 3, 7, 9, 1, 3, 7, 9, 1, 3)
        weighted_sum = 0
        for digit, weight in zip(pesel[:-1], weights):
            weighted_sum += int(str(int(digit) * weight)[-1])
        control_number = 10 - int(str(weighted_sum)[-1])

        if control_number == int(pesel[-1]):
            result = 'PESEL jest poprawny'
        else:
            result = 'PESEL jest nieprawidłowy, błędna cyfra kontrolna'

        return {
            'Wynik: ': result,
            'Data urodzenia (RRRR/MM/DD): ': f'{year}/{month}/{pesel[4:6]}',
            'Płeć: ': gender
        }

    else:
        return {'PESEL ma nieprawidłową ilość znaków: ': len(str(pesel))}
