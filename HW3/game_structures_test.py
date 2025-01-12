import unittest
from game_structures import *

class CardNodeTestCase(unittest.TestCase):
    def test_create_card_node(self):
        card_node = create_card_node("my_payload")
        ## Because this is a unit test for "create_card_node()",
        ##  I'm willing to "break the abstraction" by using `card_node['payload']` instead
        ##  of `get_card_from_node(card_node)`,
        ##  to make sure the implementation is correct.
        ## Do not do this elsewhere!
        self.assertEqual(card_node['payload'], 'my_payload')
        self.assertIsNone(card_node['prev'])
        self.assertIsNone(card_node['next'])

class DeckTestCase(unittest.TestCase):
    def test_create_deck(self):
        deck = create_deck()
        self.assertEqual(NUM_CARDS_IN_DECK, len(deck))

    def test_push_card_to_deck(self):
        deck = [] ## Using an empty "deck" to start with
        card1 = create_card(KING, SUIT_HEARTS)
        updated_deck = push_card_to_deck(deck, card1)

        self.assertIsNotNone(updated_deck)
        self.assertEqual(1, len(deck))

        card2 = create_card(QUEEN, SUIT_HEARTS)
        updated_deck = push_card_to_deck(deck, card2)

        self.assertIsNotNone(updated_deck)
        self.assertEqual(2, len(deck))

    def test_peek_deck(self):
        ## Set up
        card1 = create_card(KING, SUIT_HEARTS)
        card2 = create_card(QUEEN, SUIT_HEARTS)
        deck = [ card1, card2 ]

        ## Execute function to test
        card_on_top = peek_card(deck)

        ## Check Assertions
        self.assertIsNotNone(card_on_top)
        self.assertEqual(card2, card_on_top)
        self.assertEqual(2, len(deck))

    def test_pop_deck(self):
        ## Set up
        card1 = create_card(KING, SUIT_HEARTS)
        card2 = create_card(QUEEN, SUIT_HEARTS)
        deck = [ card1, card2 ]

        ## Execute function to test
        card_from_top = pop_card(deck)

        ## Check Assertions
        self.assertIsNotNone(card_from_top)
        self.assertEqual(card2, card_from_top)
        self.assertEqual(1, len(deck))

    def test_deck_is_empty_when_empty(self):
        ## Set up
        deck = [ ]

        ## Execute function to test
        is_empty = is_deck_empty(deck)

        ## Check Assertions
        self.assertTrue(is_empty)
        self.assertEqual(0, len(deck))

    def test_deck_is_empty_when_not_empty(self):
        ## Set up
        card1 = create_card(KING, SUIT_HEARTS)
        card2 = create_card(QUEEN, SUIT_HEARTS)
        deck = [ card1, card2 ]

        ## Execute function to test
        is_empty = is_deck_empty(deck)

        ## Check Assertions
        self.assertFalse(is_empty)
        self.assertEqual(2, len(deck))


class HandTestCase(unittest.TestCase):

    def test_create_hand(self):
        hand = create_hand()
        self.assertIsNone(get_first_card_in_hand(hand))
        self.assertEqual(get_num_cards_in_hand(hand), 0)
        self.assertTrue(is_hand_empty(hand))

    def add_1card_to_hand_test(self):
        ## Set up
        hand = create_hand()
        card = create_card(JACK, SUIT_HEARTS)

        ## Execute the thing to test
        add_card_to_hand(hand, card)

        ## Evaluate the result for correctness
        self.assertEqual(get_num_cards_in_hand(hand), 1)
        self.assertIs(get_card_from_node(get_first_card_in_hand(hand)), card)
        self.assertFalse(is_hand_empty(hand))

    def test_add_2cards_to_hand(self):
        ## Set up
        hand = create_hand()
        card = create_card(JACK, SUIT_HEARTS)
        card2 = create_card(QUEEN, SUIT_HEARTS)

        ## Execute the thing to test
        add_card_to_hand(hand, card)
        add_card_to_hand(hand, card2)

        ## Evaluate the result for correctness
        self.assertEqual(get_num_cards_in_hand(hand), 2)
        self.assertTrue(is_card_in_hand(hand, card))
        self.assertTrue(is_card_in_hand(hand, card2))
        self.assertIs(get_card_from_node(get_first_card_in_hand(hand)), card2) ## This might depend on your implementation

    def test_remove_first_card_from_hand(self):
        ## Set up
        hand = create_hand()
        card = create_card(JACK, SUIT_HEARTS)
        card2 = create_card(QUEEN, SUIT_HEARTS)
        add_card_to_hand(hand, card)
        add_card_to_hand(hand, card2) ## Gets inserted at the head

        ## Execute the thing to test
        removed_card = remove_card_from_hand(hand, card2)

        ## Evaluate the result for correctness
        self.assertEqual(get_num_cards_in_hand(hand), 1)
        self.assertTrue(is_card_in_hand(hand, card))
        self.assertFalse(is_card_in_hand(hand, card2))
        self.assertIs(removed_card, card2)
        self.assertIs(get_card_from_node(get_first_card_in_hand(hand)), card)

    def test_remove_last_card_from_hand(self):
        ## Set up
        hand = create_hand()
        card = create_card(JACK, SUIT_HEARTS)
        card2 = create_card(QUEEN, SUIT_HEARTS)
        add_card_to_hand(hand, card)
        add_card_to_hand(hand, card2)

        ## Execute the thing to test
        removed_card = remove_card_from_hand(hand, card)

        ## Evaluate the result for correctness
        self.assertEqual(get_num_cards_in_hand(hand), 1)
        self.assertFalse(is_card_in_hand(hand, card))
        self.assertTrue(is_card_in_hand(hand, card2))
        self.assertIs(removed_card, card)
        self.assertIs(get_card_from_node(get_first_card_in_hand(hand)), card2)

    def test_remove_nonexistent_card_from_hand(self):
        ## Set up
        hand = create_hand()
        card = create_card(JACK, SUIT_HEARTS)
        card2 = create_card(QUEEN, SUIT_HEARTS)
        card3 = create_card(KING, SUIT_HEARTS)
        add_card_to_hand(hand, card)
        add_card_to_hand(hand, card2)

        ## Execute the thing to test
        removed_card = remove_card_from_hand(hand, card3)

        ## Evaluate the result for correctness
        self.assertIsNone(removed_card)
        self.assertEqual(get_num_cards_in_hand(hand), 2)
        self.assertTrue(is_card_in_hand(hand, card))
        self.assertTrue(is_card_in_hand(hand, card2))

    def test_get_card_from_hand(self):
        ## Set up
        hand = create_hand()
        card = create_card(JACK, SUIT_HEARTS)
        card2 = create_card(QUEEN, SUIT_HEARTS)
        card3 = create_card(KING, SUIT_HEARTS)
        add_card_to_hand(hand, card)
        add_card_to_hand(hand, card2)
        add_card_to_hand(hand, card3)

        ## Execute the thing to test
        removed_card = get_card_from_hand(hand, 1) ## Remove the "Queen" card

        ## Evaluate the result for correctness
        self.assertEqual(2, get_num_cards_in_hand(hand))
        self.assertFalse(is_card_in_hand(hand, card2))
        self.assertTrue(is_card_in_hand(hand, card))
        self.assertTrue(is_card_in_hand(hand, card3))
        self.assertIs(card2, removed_card)

    def test_get_card_from_hand_when_empty(self):
        ## Set up
        hand = create_hand()

        ## Execute the thing to test
        removed_card = get_card_from_hand(hand, 1)

        ## Evaluate the result for correctness
        self.assertEqual(0, get_num_cards_in_hand(hand))
        self.assertIsNone(removed_card)

    def test_get_card_from_hand_when_index_is_too_big(self):
        ## Set up
        hand = create_hand()
        card = create_card(JACK, SUIT_HEARTS)
        card2 = create_card(QUEEN, SUIT_HEARTS)
        add_card_to_hand(hand, card)
        add_card_to_hand(hand, card2)

        ## Execute the thing to test
        removed_card = get_card_from_hand(hand, 3)

        ## Evaluate the result for correctness
        self.assertEqual(2, get_num_cards_in_hand(hand))
        self.assertIsNone(removed_card)

# Test cases for the functions in a3.py
class GeneralTest(unittest.TestCase):
    def test_deck(self):
        deck = create_deck()

        self.assertFalse(is_deck_empty(deck))
        self.assertEqual(len(deck), NUM_CARDS_IN_DECK)

        #print_deck(deck)

    def test_remove_hand_front(self):
        hand = create_hand()
        add_card_to_hand(hand, (JACK, SUIT_HEARTS))
        add_card_to_hand(hand, (QUEEN, SUIT_HEARTS))
        add_card_to_hand(hand, (KING, SUIT_HEARTS))
        add_card_to_hand(hand, (ACE, SUIT_HEARTS))

        remove_card_from_hand(hand, (ACE, SUIT_HEARTS))
        self.assertEqual(hand['num_cards_in_hand'], 3)
        self.assertEqual(get_card_from_node(hand['first_card']), (KING, SUIT_HEARTS))
        get_card_from_hand(hand, 0)
        self.assertEqual(hand['num_cards_in_hand'], 2)
        self.assertEqual(get_card_from_node(hand['first_card']), (QUEEN, SUIT_HEARTS))

    def test_remove_hand_middle(self):
        hand = create_hand()
        add_card_to_hand(hand, (JACK, SUIT_HEARTS))
        add_card_to_hand(hand, (QUEEN, SUIT_HEARTS))
        add_card_to_hand(hand, (KING, SUIT_HEARTS))
        add_card_to_hand(hand, (ACE, SUIT_HEARTS))

        remove_card_from_hand(hand, (KING, SUIT_HEARTS))
        self.assertEqual(hand['num_cards_in_hand'], 3)
        self.assertEqual(get_card_from_node(hand['first_card']), (ACE, SUIT_HEARTS))
        get_card_from_hand(hand, 1)
        self.assertEqual(hand['num_cards_in_hand'], 2)
        self.assertEqual(get_card_from_node(hand['first_card']), (ACE, SUIT_HEARTS))

    def test_remove_hand_end(self):
        hand = create_hand()
        add_card_to_hand(hand, (JACK, SUIT_HEARTS))
        add_card_to_hand(hand, (QUEEN, SUIT_HEARTS))
        add_card_to_hand(hand, (KING, SUIT_HEARTS))
        add_card_to_hand(hand, (ACE, SUIT_HEARTS))

        remove_card_from_hand(hand, (JACK, SUIT_HEARTS))
        self.assertEqual(hand['num_cards_in_hand'], 3)
        self.assertEqual((ACE, SUIT_HEARTS), get_card_from_node(get_first_card_in_hand(hand)))

        self.assertIsNone(get_card_from_hand(hand, 3))
        get_card_from_hand(hand, 2)
        self.assertEqual(hand['num_cards_in_hand'], 2)
        self.assertEqual((ACE, SUIT_HEARTS), get_card_from_node(get_first_card_in_hand(hand)))

    def test_remove_hand_all(self):
        hand = create_hand()
        add_card_to_hand(hand, (JACK, SUIT_HEARTS))
        add_card_to_hand(hand, (QUEEN, SUIT_HEARTS))
        add_card_to_hand(hand, (KING, SUIT_HEARTS))

        self.assertEqual((KING, SUIT_HEARTS), get_card_from_hand(hand, 0))
        self.assertEqual( (QUEEN, SUIT_HEARTS), get_card_from_hand(hand, 0))
        self.assertEqual((JACK, SUIT_HEARTS), get_card_from_hand(hand, 0))

        self.assertEqual(hand['num_cards_in_hand'], 0)
        self.assertIsNone(get_card_from_hand(hand, 0))


if __name__ == '__main__':
    unittest.main()
