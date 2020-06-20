import lettertonum


def list_convert(hole_cards, five_in_front):
    combined = []
    combined_num_letters = []
    combined_suit = []
    combined = hole_cards + five_in_front
    for card in combined:
        combined_num_letters.append(card[0])
        combined_suit.append(card[1])
    combined_num = lettertonum.letter_to_num_acehigh(combined_num_letters)
    combined_edgecase = lettertonum.letter_to_num_acelow(combined_num_letters)
    unsorted_combine_num = lettertonum.letter_to_num_acehigh(combined_num_letters)
    unsorted_combine_edgecase = lettertonum.letter_to_num_acelow(combined_num_letters)
    combined_num.sort()
    combined_edgecase.sort()
    return combined, combined_num, combined_edgecase, unsorted_combine_num, unsorted_combine_edgecase

