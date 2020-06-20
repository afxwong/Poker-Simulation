import lettertonum
import royalflush
import straightflush
import quads
import fullhouse
import normalflush
import straights
import trips
import twopair
import onepair


# Hands
# High Card
# One Pair
# Two Pair
# Trips
# Straight
# Flush
# Full House
# Quads
# Straight Flush
# Royal Flush


def hand_value(hole_cards, five_in_front):
    value = []
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

    # Royal Flush

    value.append(royalflush.royal_flush(unsorted_combine_num, combined_suit))

    # Ace to 5 Straight Flush Edge Case

    value.append(straightflush.straight_flush(unsorted_combine_edgecase, combined_suit))

    # Straight Flush

    value.append(straightflush.straight_flush(unsorted_combine_num, combined_suit))

    # Quads

    value.append(quads.quad(combined_num))

    # Full House

    value.append(fullhouse.full_house(combined_num))

    # Flush

    value.append(normalflush.flush(combined_suit))

    # Ace-5 Straight Edge Case

    value.append(straights.straight(combined_edgecase))

    # Straight

    value.append(straights.straight(combined_num))

    # Trips

    value.append(trips.trip(combined_num))

    # Two Pair

    value.append(twopair.two_pair(combined_num))

    # One Pair

    value.append(onepair.pair(combined_num))

    print(unsorted_combine_num)
    print(combined_num)
    print(combined_suit)
    print(value)
    print(max(value))

    return max(value), combined_num, combined_suit, combined_edgecase, unsorted_combine_num, \
           unsorted_combine_edgecase, value


# Testing
'''
hole = ['7C', '8C']
in_front = ['2C', '3H', '6C', '9C', 'TC']
hand_value(hole, in_front)
'''
