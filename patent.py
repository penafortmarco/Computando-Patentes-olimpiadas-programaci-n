def next_patent(patent, k):
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    letters = list(patent[:3])
    number = int(patent[3:])
    print(letters, number)
    
    while (True):
        if(k<=0): break
        number += k
        if number <= 999:
            if number == 0:
                str_number = '000'
            if number <= 9:
                str_number = '00' + str(number)
            elif number <= 99:
                str_number = '0' + str(number)
            else:
                str_number = str(number)
            break
        if number > 999:
            k = number - 999 - 1
            number = 0
            print(k)
            for i in range(len(letters)-1, -1, -1):
                if letters[i] != 'Z':
                    next_letter = alphabet.index(letters[i]) + 1
                    letters[i] = alphabet[next_letter]
                    break
                else:
                    continue

    return (str(letters) + str_number)


print(next_patent("ABC999", 1))
