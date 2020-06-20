import random
import calchandvalue
import listcombos
import tiebreaker
import tiebreakscores
import csv


def simulation():
    '''
    with open('trial1.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['My_Hand', 'Win/Lose', 'Hand_Value'])
        '''
    for iteration in range(0, 200000):
        # Initialize Variables

        deck = ['AH', '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', 'TH', 'JH', 'QH', 'KH',
                'AC', '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', 'TC', 'JC', 'QC', 'KC',
                'AS', '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', 'TS', 'JS', 'QS', 'KS',
                'AD', '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', 'TD', 'JD', 'QD', 'KD']
        my_hand = []
        opp_hand = []
        flop_turn_river = []

        # Randomize Hands
        card_ids = random.sample(range(0, 52), 12)
        # print(card_ids)
        my_hand.append(deck[card_ids[0]])
        my_hand.append(deck[card_ids[1]])
        opp_hand.append(deck[card_ids[2]])
        opp_hand.append(deck[card_ids[3]])

        # 5 cards in front

        flop_turn_river.append(deck[card_ids[5]])
        flop_turn_river.append(deck[card_ids[6]])
        flop_turn_river.append(deck[card_ids[7]])
        flop_turn_river.append(deck[card_ids[9]])
        flop_turn_river.append(deck[card_ids[11]])
        # print(flop_turn_river)

        # Import Values and Lists

        my_hand_import = calchandvalue.hand_value(my_hand, flop_turn_river)
        my_hand_value = my_hand_import[0]
        my_hands = my_hand_import[6]
        my_combined_num = my_hand_import[1]
        my_combined_suits = my_hand_import[2]
        my_unsorted_combined_num = my_hand_import[4]
        my_unsorted_combined_num_edgecase = my_hand_import[5]
        opp_hand_import = calchandvalue.hand_value(opp_hand, flop_turn_river)
        opp_hand_value = opp_hand_import[0]
        opp_hands = my_hand_import[6]
        opp_combined_num = opp_hand_import[1]
        opp_combined_suits = opp_hand_import[2]
        opp_unsorted_combined_num = opp_hand_import[4]
        opp_unsorted_combined_num_edgecase = opp_hand_import[5]

        # Declare Winner

        if my_hand_value > opp_hand_value:
            print(my_hand, opp_hand, flop_turn_river)
            print('I win')
            with open('trial5.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([str(my_hand), 'Win', str(my_hand_value)])
        if my_hand_value < opp_hand_value:
            print(my_hand, opp_hand, flop_turn_river)
            print('Opponent wins')
            with open('trial5.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([str(my_hand), 'Loss', str(my_hand_value)])

        # Dealing with a Tie
        my_tiebreak_score = 0
        opp_tiebreak_score = 0
        if my_hand_value == opp_hand_value:
            my_score, opp_score = tiebreakscores.tie_scores(my_hands, opp_hands, my_hand_value, opp_hand_value,
                                                            my_combined_suits,
                                                            opp_combined_suits, my_combined_num, opp_combined_num,
                                                            my_unsorted_combined_num,
                                                            opp_unsorted_combined_num, my_tiebreak_score,
                                                            opp_tiebreak_score)
            print(my_score, opp_score)
            if my_score == opp_score:
                print(my_hand, opp_hand, flop_turn_river)
                print('Chop')
                with open('trial5.csv', 'a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([str(my_hand), 'Tie', str(my_hand_value)])
            if my_score > opp_score:
                print(my_hand, opp_hand, flop_turn_river)
                print('I win on Tiebreaker')
                with open('trial5.csv', 'a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([str(my_hand), 'Win', str(my_hand_value)])
            if my_score < opp_score:
                print(my_hand, opp_hand, flop_turn_river)
                print('Opponent wins on Tiebreaker')
                with open('trial5.csv', 'a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([str(my_hand), 'Loss', str(my_hand_value)])


simulation()
