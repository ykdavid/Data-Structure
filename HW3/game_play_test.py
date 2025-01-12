import unittest

from game_play import *


class DeckTestCase(unittest.TestCase):
    def test_create_deck(self):
        # Set up
        deck = create_deck()
        orig_list = deck[:]

        # Run the thing to test
        shuffle(deck)

        # Observe and check that things are as expected
        self.assertNotEqual(orig_list, deck)

    def test_deal(self):
        deck = create_deck()
        hand1 = create_hand()
        hand2 = create_hand()

        deal(deck, hand1, hand2)

        self.assertEqual(len(deck), NUM_CARDS_IN_DECK - 2 * (NUM_CARDS_IN_HAND))
        self.assertEqual(hand1['num_cards_in_hand'], NUM_CARDS_IN_HAND)
        self.assertEqual(hand2['num_cards_in_hand'], NUM_CARDS_IN_HAND)

    def test_return_hand_to_deck(self):
        deck = create_deck()
        hand1 = create_hand()
        hand2 = create_hand()
        deal(deck, hand1, hand2)

        return_hand_to_deck(hand1, deck)

        self.assertEqual(NUM_CARDS_IN_DECK - NUM_CARDS_IN_HAND, len(deck))
        self.assertTrue(is_hand_empty(hand1))

        return_hand_to_deck(hand2, deck)
        self.assertEqual(NUM_CARDS_IN_DECK, len(deck))
        self.assertTrue(is_hand_empty(hand1))



class GameTestCase(unittest.TestCase):
    def test_is_legal_move(self):
        hand = create_hand()
        add_card_to_hand(hand, ('King', 'of', 'Clubs'))
        add_card_to_hand(hand, (10, 'of', 'Spades'))
        add_card_to_hand(hand, (9, 'of', 'Hearts'))
        add_card_to_hand(hand, ('Queen', 'of', 'Diamonds'))

        result = is_legal_move(hand, ('Ace', 'of', 'Clubs'), (10, 'of', 'Clubs'))

        self.assertTrue(result)

        result = is_legal_move(hand, ('Ace', 'of', 'Clubs'), (10, 'of', 'Diamonds'))
        self.assertFalse(result)

    def test_who_won(self):
        ## How this test is set up might depend how you implement your cards
        ## It can be okay to change it
        lead_card = ('Ace', 'of', 'Clubs', 14)
        followed_card = (9, 'of', 'Clubs', 9)
        trump = 'Hearts'

        result = who_won(lead_card, followed_card, trump)
        self.assertTrue(result)

        result = who_won( (9, 'of', 'Clubs', 9), ('Ace', 'of', 'Diamonds', 14), 'Diamonds')
        self.assertFalse(result)

        result = who_won( (9, 'of', 'Clubs', 9), ('Ace', 'of', 'Diamonds', 14), 'Clubs')
        self.assertTrue(result)

    def test_sort_hand_full_hand_with_trump(self):
        ## Set up
        trump = SUIT_CLUBS
        hand = create_hand()
        card = create_card(JACK, SUIT_HEARTS)
        card2 = create_card(QUEEN, SUIT_HEARTS)
        card3 = create_card(KING, SUIT_HEARTS)
        trump_card4 = create_card(KING, SUIT_CLUBS)
        card5 = create_card(KING, SUIT_SPADES)
        add_card_to_hand(hand, card)
        add_card_to_hand(hand, card2)
        add_card_to_hand(hand, card3)
        add_card_to_hand(hand, trump_card4)
        add_card_to_hand(hand, card5)

        sort_hand(hand, trump)

        self.assertEqual(trump_card4, get_card_from_node(get_first_card_in_hand(hand)))
        self.assertEqual(card5, get_card_from_hand_at_index(hand, 1))
        self.assertEqual(card3, get_card_from_hand_at_index(hand, 2))
        self.assertEqual(card2, get_card_from_hand_at_index(hand, 3))
        self.assertEqual(card, get_card_from_hand_at_index(hand, 4))

    def test_swap_card_with_next_middle(self):
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

        swap_card_with_next(hand, 0)

        self.assertEqual(card4, get_card_from_hand_at_index(hand, 0))
        self.assertEqual(card5, get_card_from_hand_at_index(hand, 1))
        self.assertEqual(card3, get_card_from_hand_at_index(hand, 2))
        self.assertEqual(card2, get_card_from_hand_at_index(hand, 3))
        self.assertEqual(card, get_card_from_hand_at_index(hand, 4))

    def test_swap_card_with_next_end(self):
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




if __name__ == '__main__':
    unittest.main()
