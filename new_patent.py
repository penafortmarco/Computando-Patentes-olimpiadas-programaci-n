from common import *

def get_new_patent_format(patent, k):
    try:
        first_letters = list(patent[:2])
        number = int(patent[2:5])
        last_letters = list(patent[5:])
    except (ValueError):
            error_message = 'Not a valid patent'
            return error_message
            
    (result_last_letters, number_increment) = get_new_patent_letters(last_letters, k, False)
    (result_number, letter_increment) = get_patent_numbers(number + number_increment)
    result_first_letters = get_new_patent_letters(first_letters, letter_increment, True)
    result_number = number_to_str(result_number)

    return (result_first_letters + result_number + result_last_letters)

def get_new_patent_letters(letters, increment, is_first):

    index_1 = alphabet.index(letters[1])
    index_0 = alphabet.index(letters[0])

    (letter_1, increment_number_1) = get_letter_and_increment(index_1 + increment, alphabet_size)
    (letter_0, increment_number_0) = get_letter_and_increment(index_0 + increment_number_1, alphabet_size)
    if is_first:
        if increment_number_0 > 0:
            if increment_number_0 > 0:
             raise Exception('Patent does not exist')
        else:
            return ''.join(list(letter_0 + letter_1))
    else:
        return (''.join(list(letter_0 + letter_1)), increment_number_0)