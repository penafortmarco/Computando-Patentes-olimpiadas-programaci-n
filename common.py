alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
alphabet_size = len(alphabet)

def get_patent_numbers(increment):
    (result_number, increment_letter) = int_division(increment, 1000)
    return (result_number, increment_letter)

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
