#global variables
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
alphabet_size = len(alphabet)


def get_patent_numbers(increment):
    """Calls the int_division with the increment(patent number + k) as first argument and 1000 as the second argument.
    it will return the new patent number as the rest and the increment of letters."""

    (result_number, increment_letter) = int_division(increment, 1000)
    return (result_number, increment_letter)


def int_division(number, divider):
    """Return a result and a rest of a int division (no decimals)"""

    result_number = number % divider
    increment_letter = number // divider

    return (result_number, increment_letter)


def get_letter_and_increment(number, divider):
    """Calls int_division with the increment and a total. After that, it will return an index for replace the letter.
    Then return the new_letter and the increment of the next letter (It could be 0)."""

    if divider == 0:
        return (number, 0)
    (new_index, increment) = int_division(number, divider)
    new_letter = alphabet[new_index]

    return (new_letter, increment)


def number_to_str(number):
    """It transform the input number to string in a right format for the patent.
    Example: if number = 1 it returns 001. Else case just transform number to string and allow to concatenate with another str."""

    if number == 0:
        str_number = '000'
    if number <= 9:
        str_number = '00' + str(number)
    elif number <= 99:
        str_number = '0' + str(number)
    else:
        str_number = str(number)

    return str_number
