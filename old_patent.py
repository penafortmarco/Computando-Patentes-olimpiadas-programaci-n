from common import *

def get_old_patent_format(patent, k):
    """Convert patent in 2 different lists for number and for letters. Calls the function get_patent_numbers that return 
    in a tuple result_number that is the final number in the patent and increment_letter, that is the number of letters it 
    has to be added. Calls the function get_old_pattent_letters if is necessary. Finally return a str with the full patent"""

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
    """Take the index (int) of each letter in the list according to alphabet. Then call the function get_letter_and_increment
    to calculate every letter. It will return the new letter and an increment for the next letter if it is necessary. If the 
    last increment (increment_number_0) is greater than 0 it means that there is no patent "k" positions after the original patent.
    Return a list with the new_letters"""

    index_2 = alphabet.index(letters[2])
    index_1 = alphabet.index(letters[1])
    index_0 = alphabet.index(letters[0])

    (letter_2, increment_number_2) = get_letter_and_increment(index_2 + increment, alphabet_size)
    (letter_1, increment_number_1) = get_letter_and_increment(index_1 + increment_number_2, alphabet_size)
    (letter_0, increment_number_0) = get_letter_and_increment(index_0 + increment_number_1, alphabet_size)

    if increment_number_0 > 0:
        raise Exception('Patent does not exist')

    return letter_0 + letter_1 + letter_2