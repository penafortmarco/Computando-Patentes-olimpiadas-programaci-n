alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


def next_patent(patent, k):
    """Validates the right format for the patent. It also manage error cases.
    Then call the functions that are needed to return the next "k" patent."""

    if len(patent) < 6 or len(patent) > 7:
        error_message = 'Not a valid patent.'
        return error_message
    if k <= 0:
        error_message = 'K is not a valid argument.'
        return error_message

    if len(patent) == 6:
        return old_patent_format(patent, k)


def old_patent_format(patent, k):
    """Transform the patent in the old format patent. Then calculates numbers and letters 
    that i have to add after "k" times. If incremente > 999 it means that will at least
    one letter to add. Else case means that only numbers have to be added. Lastly return 
    letters and numbers in a str."""
    
    try:
        letters = list(patent[:3])
        number = int(patent[3:])
        increment = (number + k)
    except(ValueError):
        error_message = 'Not a valid patent'
        return error_message

    increment_number = (increment % 1000)
    increment_letter = (increment // 1000)

    if (increment) > 999:
        increment_letter = old_patent_letters(letters, increment_letter)
    else:
        increment_letter = letters
    increment_number = number_to_str(increment_number)

    return (increment_letter + increment_number)


def old_patent_letters(letters, increment):
    """Takes the original letters of the patent and check the last one first and increase
    according to the var increment. Then, the letter will move n positions from the index
    to find the next letter. The other results indicate if the next letters has to be modified.
    Finally, it returns a str with all letter concatenated."""

    index_2 = alphabet.index(letters[2])
    index_1 = alphabet.index(letters[1])
    index_0 = alphabet.index(letters[0])

    result_2 = (index_2 + increment) % 26
    result_1 = (index_2 + increment) // 26
    result_0 = (index_1 + increment) // 26

    letter_2 = alphabet[result_2]
    letter_1 = alphabet[index_1 + result_1]
    letter_0 = alphabet[index_0 + result_0]

    return ''.join(letter_0 + letter_1 + letter_2)


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




