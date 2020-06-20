def letter_to_num_acehigh(num_list):
    numify_list = []
    for el in num_list:
        if el == 'T':
            numify_list.append(10)
        elif el == 'J':
            numify_list.append(11)
        elif el == 'Q':
            numify_list.append(12)
        elif el == 'K':
            numify_list.append(13)
        elif el == 'A':
            numify_list.append(14)
        else:
            numify_list.append(int(el))
    return numify_list


def letter_to_num_acelow(num_list):
    numify_list = []
    for el in num_list:
        if el == 'T':
            numify_list.append(10)
        elif el == 'J':
            numify_list.append(11)
        elif el == 'Q':
            numify_list.append(12)
        elif el == 'K':
            numify_list.append(13)
        elif el == 'A':
            numify_list.append(1)
        else:
            numify_list.append(int(el))
    return numify_list


