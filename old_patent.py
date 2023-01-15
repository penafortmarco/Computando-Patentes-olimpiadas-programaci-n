from common import *

def get_old_patent_format(patent, k):
    """"""
    try:
        letters = list(patent[:3])
        number = int(patent[3:])
        increment = (number + k)
    except (ValueError):
        error_message = 'Not a valid patent'
        return error_message

    (result_number, increment_letter) = get_patent_numbers(increment)

    if increment_letter > 0:
        letters = get_old_patent_letters(letters, increment_letter)

    new_number = number_to_str(result_number)

    return (''.join(letters) + new_number)

def get_old_patent_letters(letters, increment):
    """"""

    index_2 = alphabet.index(letters[2])
    index_1 = alphabet.index(letters[1])
    index_0 = alphabet.index(letters[0])

    (letter_2, increment_number_2) = get_letter_and_increment(index_2 + increment, alphabet_size)
    (letter_1, increment_number_1) = get_letter_and_increment(index_1 + increment_number_2, alphabet_size)
    (letter_0, increment_number_0) = get_letter_and_increment(index_0 + increment_number_1, alphabet_size)

    if increment_number_0 > 0:
        raise Exception('Patent does not exist')

    return str(letter_0) + str(letter_1) + str(letter_2)