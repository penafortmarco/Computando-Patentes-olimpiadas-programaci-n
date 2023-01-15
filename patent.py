alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
alphabet_size = len(alphabet)

def next_patent(patent, k):
    """Validates the right format for the patent. It also manage error cases.
    Then call the functions that are needed to return the next "k" patent."""
    if len(patent) < 6 or len(patent) > 7:
            error_message = 'Not a valid patent.'
            return error_message
    if k <= 0 or type(k) != int:
        error_message = 'K is not a valid argument.'
        return error_message
    
    try:
        if len(patent) == 6:
            return get_old_patent_format(patent, k)
        if len(patent) == 7:
            return get_new_patent_format(patent, k)
    except Exception as e:
        print(e)


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


def get_patent_numbers(increment):
    (result_number, increment_letter) = int_division(increment, 1000)
    return (result_number, increment_letter)


def get_old_patent_letters(letters, increment):
    """Takes the original letters of the patent and check the last one first and increase
    according to the var increment. Then, the letter will move n positions from the index
    to find the next letter. The other results indicate if the next letters has to be modified.
    Finally, it returns a str with all letter concatenated."""

    index_2 = alphabet.index(letters[2])
    index_1 = alphabet.index(letters[1])
    index_0 = alphabet.index(letters[0])

    (letter_2, increment_number_2) = get_letter_and_increment(
        index_2 + increment, alphabet_size)
    (letter_1, increment_number_1) = get_letter_and_increment(
        index_1 + increment_number_2, alphabet_size)
    (letter_0, increment_number_0) = get_letter_and_increment(
        index_0 + increment_number_1, alphabet_size)
    if increment_number_0 > 0:
        raise Exception('Se re fue')

    return str(letter_0) + str(letter_1) + str(letter_2)


def int_division(number, divider):
    result_number = number % divider
    increment_number = number // divider

    return (result_number, increment_number)


def get_index_letter_and_increment(number, divider):
    (number, divider) = int_division(number, divider)
    return (number, divider)


def get_letter_and_increment(number, divider):
    if divider == 0:
        return (number, 0)
    (number, increment) = get_index_letter_and_increment(number, divider)
    letter = alphabet[number]

    return (letter, increment)


def get_new_patent_format(patent, k):
    first_letters = list(patent[:2])
    number = int(patent[2:5])
    last_letters = list(patent[5:])

    (result_last_letters, number_increment) = get_new_patent_letters(
        last_letters, k, False)
    (result_number, letter_increment) = get_patent_numbers(number + number_increment)
    result_first_letters = get_new_patent_letters(
        first_letters, letter_increment, True)
    result_number = number_to_str(result_number)

    return (result_first_letters + result_number + result_last_letters)


def get_new_patent_letters(letters, increment, is_first):

    index_1 = alphabet.index(letters[1])
    index_0 = alphabet.index(letters[0])

    (letter_1, increment_number_1) = get_letter_and_increment(
        index_1 + increment, alphabet_size)
    (letter_0, increment_number_0) = get_letter_and_increment(
        index_0 + increment_number_1, alphabet_size)
    if is_first:
        if increment_number_0 > 0:
            # tirar error, no existen más patentes
            pass
        else:
            return ''.join(list(letter_0 + letter_1))
    else:
        return (''.join(list(letter_0 + letter_1)), increment_number_0)


def number_to_str(number):
    """It transform the input number to string in a right format for the patent.
    Example: if number = 1 it returns 001. Else case just transform number to 
    string and allow to concatenate with another str."""

    if number == 0:
        str_number = '000'
    if number <= 9:
        str_number = '00' + str(number)
    elif number <= 99:
        str_number = '0' + str(number)
    else:
        str_number = str(number)

    return str_number
