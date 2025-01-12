import unittest
from game_play import *
def print_hand_detail(hand):
    print('====')
    cur_card_node = hand['first_card']
    while cur_card_node is not None:
        card = cur_card_node['payload']
        prev_node = cur_card_node['prev']
        next_node = cur_card_node['next']
        prev_card = prev_node['payload'] if prev_node else None
        next_card = next_node['payload'] if next_node else None
        #print(f"Current Node: {cur_card_node}")
        print(f"Card: {card} of {card[1]}, prev: {prev_card}, next: {next_card}")
        cur_card_node = cur_card_node['next']
    print('====')

class TestGamePlay(unittest.TestCase):

    def test_sort_hand_full_hand_with_trump(self):
        # Set up
        trump = SUIT_CLUBS
        hand = create_hand()
        card = create_card(JACK, SUIT_HEARTS)
        card2 = create_card(QUEEN, SUIT_HEARTS)
        card3 = create_card(KING, SUIT_HEARTS)
        trump_card4 = create_card(KING, SUIT_CLUBS)
        card5 = create_card(KING, SUIT_SPADES)
        
        # Adding cards to hand with print statements
        add_card_to_hand(hand, card)
        add_card_to_hand(hand, card2)
        add_card_to_hand(hand, card3)
        add_card_to_hand(hand, trump_card4)
        add_card_to_hand(hand, card5)

        # Print hand before sorting
        print("\nHand before sorting:")
        print_hand_detail(hand)

        # Sort the hand by trump
        print("\nSorting the hand by trump:")
        sort_hand(hand, trump)

        # Print hand after sorting
        print("\nHand after sorting:")
        print_hand_detail(hand)
        print('------------')
        # Assertions to verify the correct order after sorting
        self.assertEqual(trump_card4, get_card_from_node(0))#get_first_card_in_hand(hand)))
        self.assertEqual(card5, get_card_from_hand_at_index(hand, 1))
        self.assertEqual(card3, get_card_from_hand_at_index(hand, 2))
        self.assertEqual(card2, get_card_from_hand_at_index(hand, 3))
        self.assertEqual(card, get_card_from_hand_at_index(hand, 4))
'''

    def test_swap_card_with_next_middle(self):
        print("test_swap_card_with_next_middle")
        hand = create_hand()
        card = create_card(JACK, SUIT_HEARTS)
        card2 = create_card(QUEEN, SUIT_HEARTS)
        card3 = create_card(KING, SUIT_HEARTS)
        card4 = create_card(KING, SUIT_CLUBS)
        card5 = create_card(KING, SUIT_SPADES)
        add_card_to_hand(hand, card)
        add_card_to_hand(hand, card2)
        add_card_to_hand(hand, card3)
        add_card_to_hand(hand, card4)
        add_card_to_hand(hand, card5)
        swap_card_with_next(hand, 1)
        self.assertEqual(card5, get_card_from_hand_at_index(hand, 0))
        self.assertEqual(card3, get_card_from_hand_at_index(hand, 1))
        self.assertEqual(card4, get_card_from_hand_at_index(hand, 2))
        self.assertEqual(card2, get_card_from_hand_at_index(hand, 3))
        self.assertEqual(card, get_card_from_hand_at_index(hand, 4))

    def test_swap_card_with_next_beginning(self):
        print("test_swap_card_with_next_beginning")
        hand = create_hand()
        card = create_card(JACK, SUIT_HEARTS)
        card2 = create_card(QUEEN, SUIT_HEARTS)
        card3 = create_card(KING, SUIT_HEARTS)
        card4 = create_card(KING, SUIT_CLUBS)
        card5 = create_card(KING, SUIT_SPADES)
        add_card_to_hand(hand, card)
        add_card_to_hand(hand, card2)
        add_card_to_hand(hand, card3)
        add_card_to_hand(hand, card4)
        add_card_to_hand(hand, card5)

        print_hand(hand)

        swap_card_with_next(hand, 0)

        print_hand(hand)

        self.assertEqual(card4, get_card_from_hand_at_index(hand, 0))
        self.assertEqual(card5, get_card_from_hand_at_index(hand, 1))
        self.assertEqual(card3, get_card_from_hand_at_index(hand, 2))
        self.assertEqual(card2, get_card_from_hand_at_index(hand, 3))
        self.assertEqual(card, get_card_from_hand_at_index(hand, 4))

    def test_swap_card_with_next_end(self):
        print("test_swap_card_with_next_end")
        hand = create_hand()
        card = create_card(JACK, SUIT_HEARTS)
        card2 = create_card(QUEEN, SUIT_HEARTS)
        card3 = create_card(KING, SUIT_HEARTS)
        card4 = create_card(KING, SUIT_CLUBS)
        card5 = create_card(KING, SUIT_SPADES)
        add_card_to_hand(hand, card)
        add_card_to_hand(hand, card2)
        add_card_to_hand(hand, card3)
        add_card_to_hand(hand, card4)
        add_card_to_hand(hand, card5)

        swap_card_with_next(hand, 4)

        self.assertEqual(card5, get_card_from_hand_at_index(hand, 0))
        self.assertEqual(card4, get_card_from_hand_at_index(hand, 1))
        self.assertEqual(card3, get_card_from_hand_at_index(hand, 2))
        self.assertEqual(card2, get_card_from_hand_at_index(hand, 3))
        self.assertEqual(card, get_card_from_hand_at_index(hand, 4))

    '''
# This will run the test and print card information
if __name__ == '__main__':
    unittest.main()
