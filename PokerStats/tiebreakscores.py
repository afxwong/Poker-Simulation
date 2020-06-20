import tiebreaker


def compare(x, y):
    while len(x) > 0:
        if x[-1] > y[-1] or y[-1] > x[-1]:
            return x[-1], y[-1]
        elif x[-1] == y[-1]:
            x.remove(x[-1])
            y.remove(y[-1])
            compare(x, y)
    else:
        return 50, 50


def tie_scores(my_hands, opp_hands, my_hand_value, opp_hand_value, my_combined_suits, opp_combined_suits,
               my_combined_num, opp_combined_num, my_unsorted_combined_num, opp_unsorted_combined_num, my_tiebreak_score, opp_tiebreak_score):
    if my_hand_value == 10:
        my_tiebreak_score = 10
        opp_tiebreak_score = 10
        return my_tiebreak_score, opp_tiebreak_score
    if my_hand_value == 9 and my_hands[1] != 0 and opp_hands[1] != 0:
        my_tiebreak_score = 5
        opp_tiebreak_score = 5
        return my_tiebreak_score, opp_tiebreak_score
    elif my_hand_value == 9 and my_hands[1] == 0 and opp_hands[1] == 0:
        my_tiebreak_score = tiebreaker.straight_flush(my_unsorted_combined_num, my_combined_suits)
        opp_tiebreak_score = tiebreaker.straight_flush(opp_unsorted_combined_num, opp_combined_suits)
        return my_tiebreak_score, opp_tiebreak_score
    elif my_hand_value == 8:
        my_tiebreak_score = tiebreaker.quads(my_combined_num)
        opp_tiebreak_score = tiebreaker.quads(opp_combined_num)
        return my_tiebreak_score, opp_tiebreak_score
    elif my_hand_value == 7:
        my_fh = tiebreaker.full_house(my_combined_num)
        opp_fh = tiebreaker.full_house(opp_combined_num)
        my_tiebreak_score = my_fh[1]  # Kickers
        opp_tiebreak_score = opp_fh[1]
        return my_tiebreak_score, opp_tiebreak_score
    elif my_hand_value == 6:
        my_tiebreak_score = tiebreaker.flush(my_unsorted_combined_num, my_combined_suits)
        opp_tiebreak_score = tiebreaker.flush(opp_unsorted_combined_num, opp_combined_suits)
        return my_tiebreak_score, opp_tiebreak_score
    elif my_hand_value == 5 and my_hands[6] != 0 and opp_hands[6] != 0:
        my_tiebreak_score = 5
        opp_tiebreak_score = 5
        return my_tiebreak_score, opp_tiebreak_score
    elif my_hand_value == 5:
        my_tiebreak_score = tiebreaker.straight(my_combined_num)
        opp_tiebreak_score = tiebreaker.straight(opp_combined_num)
        return my_tiebreak_score, opp_tiebreak_score
    elif my_hand_value == 4:
        my_return = tiebreaker.trips(my_combined_num)
        opp_return = tiebreaker.trips(opp_combined_num)
        if my_return[0] != opp_return[0]:
            return my_return[0], opp_return[0]
        elif my_return[0] == opp_return[0] and my_return[1] == opp_return[1]:
            return my_return[0], opp_return[0]
        else:
            my_tiebreak_score, opp_tiebreak_score = compare(my_return[1], opp_return[1])
            return my_tiebreak_score, opp_tiebreak_score
    elif my_hand_value == 3:
        my_return = tiebreaker.two_pair(my_combined_num)
        opp_return = tiebreaker.two_pair(opp_combined_num)
        if my_return[0] != opp_return[0]:
            return my_return[0], opp_return[0]
        elif my_return[0] == opp_return[0] and my_return[1] != opp_return[1]:
            return my_return[1], opp_return[1]
        else:
            return my_return[2], opp_return[2]
    elif my_hand_value == 2:
        my_return = tiebreaker.one_pair(my_combined_num)
        opp_return = tiebreaker.one_pair(opp_combined_num)
        if my_return[0] != opp_return[0]:
            return my_return[0], opp_return[0]
        elif my_return[0] == opp_return[0] and my_return[1] == opp_return[1]:
            return my_return[0], opp_return[0]
        else:
            my_tiebreak_score, opp_tiebreak_score = compare(my_return[1], opp_return[1])
            return my_tiebreak_score, opp_tiebreak_score
    elif my_hand_value == 0:
        print(my_combined_num, opp_combined_num)
        my_tiebreak_score, opp_tiebreak_score = compare(my_combined_num, opp_combined_num)
        return my_tiebreak_score, opp_tiebreak_score
