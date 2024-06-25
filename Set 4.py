def bin_to_dec(binary_string):

    integer_list = [int(digit) for digit in binary_string]

    counter = 0
    binary = 0

    while counter < len(integer_list):
        a = integer_list[counter]*(2**(len(integer_list)-1-counter))
        counter += 1
        binary += a
    
    return binary

def dec_to_bin(number):

    listed = [number]

    while number > 1:
        number //= 2
        listed.append(number)

    arranged = listed [::-1]

    odd_or_even = ''.join([str(0) if arranged[i] % 2 == 0 else str(1) for i in range(len(arranged))])

    return odd_or_even

def telephone_cipher(message):

    encoder_dict = {
            " ":"0",
            "A":"2",
            "B":"22",
            "C":"222",
            "D":"3",
            "E":"33",
            "F":"333",
            "G":"4",
            "H":"44",
            "I":"444",
            "J":"5",
            "K":"55",
            "L":"555",
            "M":"6",
            "N":"66",
            "O":"666",
            "P":"7",
            "Q":"77",
            "R":"777",
            "S":"7777",
            "T":"8",
            "U":"88",
            "V":"888",
            "W":"9",
            "X":"99",
            "Y":"999",
            "Z":"9999"
        }
    
    counter = 0
    new_form = ""

    while counter < len(message) - 1:
        if encoder_dict[message[counter]][0] == encoder_dict[message[counter+1]][0]:
            encoded_number = encoder_dict[message[counter]]
            new_form += encoded_number + "_"

        else:
            encoded_number = encoder_dict[message[counter]]
            new_form += encoded_number

        counter += 1

    new_form += encoder_dict[message[counter]]
            
    return new_form

def telephone_decipher(telephone_string):

    decipher_dict = {
            "0":" ",
            '2': 'A',
            '22': 'B',
            '222': 'C',
            '3': 'D',
            '33': 'E',
            '333': 'F',
            '4': 'G',
            '44': 'H',
            '444': 'I',
            '5': 'J',
            '55': 'K',
            '555': 'L',
            '6': 'M',
            '66': 'N',
            '666': 'O',
            '7': 'P',
            '77': 'Q',
            '777': 'R',
            '7777': 'S',
            '8': 'T',
            '88': 'U',
            '888': 'V',
            '9': 'W',
            '99': 'X',
            '999': 'Y',
            '9999': 'Z'
        }

    moving = 0
    start = 0
    expanded = []

    while moving < len(telephone_string):

        if telephone_string[start] == telephone_string[moving]:
            moving += 1
            if moving == len(telephone_string):
                sublist = telephone_string[start:moving]
                expanded.append(sublist)
                break
        else:
            sublist = telephone_string[start:moving]
            expanded.append(sublist)
            start = moving

    clean_expanded = []
    counter = 0
    while counter < len(expanded):

        if expanded[counter] == "_":
            counter += 1
        else:
            clean_expanded.append(expanded[counter])
            counter += 1

    result = [decipher_dict[clean_expanded[i]] for i in range(len(clean_expanded))]
 
    return ''.join(result)