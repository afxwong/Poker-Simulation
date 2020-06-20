def flush(suits):
    clubs = suits.count('C')
    diamonds = suits.count('D')
    hearts = suits.count('H')
    spades = suits.count('S')
    if clubs >= 5:
        return 6
    elif diamonds >= 5:
        return 6
    elif hearts >= 5:
        return 6
    elif spades >= 5:
        return 6
    else:
        return 0

# Testing
'''
s = ['D', 'H', 'C', 'S', 'D']
flush(s)
ss = ['S', 'S', 'S', 'C', 'H', 'S', 'S']
flush(ss)
'''
