


#  Copyright (c) 2024.

## These constants have been defined as a starting point.
## You may find yourself wanting to define things a little differently for your
##  implementation. That's fine.
NUM_CARDS_IN_HAND = 5
NUM_CARDS_IN_DECK = 24

SUIT_CLUBS = 'Clubs'
SUIT_SPADES = 'Spades'
SUIT_HEARTS = 'Hearts'
SUIT_DIAMONDS = 'Diamonds'

JACK = 'Jack'
QUEEN = 'Queen'
KING = 'King'
ACE = 'Ace'
VAL_9 = '9'
VAL_10 = '10'

SUITS = [SUIT_CLUBS, SUIT_SPADES, SUIT_HEARTS, SUIT_DIAMONDS]
FACES = [JACK, QUEEN, KING, ACE]
NUMBERED = [VAL_9, VAL_10]
COLOR_BLACK = 'BLACK'
COLOR_RED = 'RED'

CARD_TO_VALUE_MAP = {
	VAL_9: 9,
	VAL_10: 10,
	JACK: 11,
	QUEEN: 12,
	KING: 13,
	ACE: 14
}

## card is a tuple of (name, suit, color, value)

## deck is a list structured as a stack

## card_node is a dict of {next_card, prev_card, payload}

## hand is a linked list, represented by a dict of {first_card, num_cards_in_hand}

# ----------------------------------------
#  Deck functions
# ---------------------------------------
#  Assume that the value of cards are:
#  Nine=9; Ten=10; Jack=11; and so on, up to Ace=14.
def create_card(card, suit):
	card_name = '{face} of {suit}'.format(face = card, suit = suit)
	card_color = COLOR_RED if suit in [SUIT_HEARTS, SUIT_DIAMONDS] else COLOR_BLACK
	return (card_name, suit, card_color, CARD_TO_VALUE_MAP[card])

# Creates the deck, initializing any fields necessary.
# Returns a deck.
def create_deck():
	deck = []
	for suit in SUITS:
		for card in FACES + NUMBERED:
			deck.append(create_card(card, suit))
	return deck

# Adds a card to the top of the deck.
# Returns the deck.
def push_card_to_deck(deck, card):
	deck.append(card)
	return deck

# Shows the top card, but does not remove it from the stack.
# Returns the top card.
def peek_card(deck):
	if len(deck)>0:
		return deck[-1]
	return None

# Removes the top card from the deck and returns it.
# Returns to the top card in the deck.
def pop_card(deck):
	if len(deck)>0:
		return deck.pop()
	return None

# Determines if the deck is empty.
# Returns True if the Deck has any cards; False otherwise.
def is_deck_empty(deck):
	return len(deck) == 0

## Prints the provided deck
## Do a little more than just calling "print()"-- make it look nice!
def print_deck(deck):
	for card in deck:
		print('{face} of {suit} ({color})'.format(face=card[0], suit=card[1], color=card[2]))

#----------------------------------------
# Hand functions
#----------------------------------------

## A Hand is a linked list, so we define Card_Nodes before
## defining the Hand

def create_card_node(card):
	return { 'payload': card,
			 'next': None,
			 'prev': None }

def get_next_card_node(card_node):
	if card_node:
		return card_node['next']
	return None

def set_next_card_node(card_node_src, card_node_dest):
	if card_node_src:
		card_node_src['next']=card_node_dest

def get_prev_card_node(card_node):
	if card_node:
		return card_node['prev']
	return None

def set_prev_card_node(card_node_src, card_node_dest):
	if card_node_src:
		card_node_src['prev']=card_node_dest

def get_card_from_node(card_node):
	if card_node:
		return card_node['payload']
	return None

# Creates a Hand and initializes any necessary fields.
# Returns a new empty hand
def create_hand():
	return {'first_card': None,
			'num_cards_in_hand': 0}

def get_first_card_in_hand(hand):
	if hand:
		return hand['first_card']
	return None

def set_first_card_in_hand(hand, new_first_card_node):
	if hand:
		hand['first_card'] = new_first_card_node

def get_num_cards_in_hand(hand):
	if hand:
		return hand['num_cards_in_hand']
	return None

def increment_num_cards_in_hand(hand):
	hand['num_cards_in_hand'] += 1

def decrement_num_cards_in_hand(hand):
	hand['num_cards_in_hand'] -= 1

# Adds a card to the hand.
def add_card_to_hand(hand, card):
	new_card_node=create_card_node(card)
	if is_hand_empty(hand):
		set_first_card_in_hand(hand,new_card_node)
	else:
		first_card_node = get_first_card_in_hand(hand)
		new_card_node['next']= first_card_node
		#new_card_node['prev']=first_card_node['prev']
		first_card_node['prev']=new_card_node
		set_first_card_in_hand(hand, new_card_node)
	increment_num_cards_in_hand(hand)
     

# Removes a card from the hand via card value
# Returns the card (not a card_node) that was removed from the hand
# Returns None if the specified card is not in the hand
def remove_card_from_hand(hand, card):
	current_node = get_first_card_in_hand(hand)
	while(current_node is not None):
		if get_card_from_node(current_node) == card:
			if current_node['prev'] is not None:
				current_node['prev']['next'] = current_node['next']
    
			if current_node['next'] is not None:
				current_node['next']['prev'] = current_node['prev']
    
			if current_node == get_first_card_in_hand(hand):
				set_first_card_in_hand(hand, current_node['next'])
          
			decrement_num_cards_in_hand(hand)
			return card
		current_node = get_next_card_node(current_node)
	return None
          
            
 


# Removes a card from the hand via index
# Returns the card, not a card_node
# Returns None if index is < 0 or greater than the length of the hand/list.
def get_card_from_hand(hand, index):
    if index < 0 or index >= get_num_cards_in_hand(hand):
        return None
    current_node = get_first_card_in_hand(hand)
    current_index = 0

    # Traverse to the card at the given index
    while current_node is not None:
        if current_index == index:
            # Remove the card node from the linked list
            
            if current_node['prev'] is not None:
                current_node['prev']['next'] = current_node['next']
            if current_node['next'] is not None:
                current_node['next']['prev'] = current_node['prev']
            if current_node == get_first_card_in_hand(hand):
                set_first_card_in_hand(hand, current_node['next'])
            
            decrement_num_cards_in_hand(hand)
            
            return get_card_from_node(current_node)
        current_node = get_next_card_node(current_node)
        current_index += 1
    return None

# Returns the card in the hand at the specified index
# Returns the card, not a card_node
# Returns None if index is < 0 or greater than the length of the hand/list.
def get_card_from_hand_at_index(hand, index):
    if index < 0 or index >= get_num_cards_in_hand(hand):
        return None
    current_node = get_first_card_in_hand(hand)
    current_index = 0

    # Traverse to the card at the given index
    while current_node is not None:
        if current_index == index:
            return get_card_from_node(current_node)
        current_node = get_next_card_node(current_node)
        current_index += 1
    return None

def is_card_in_hand(hand, card):
	current_node = get_first_card_in_hand(hand)
	while current_node is not None:
		if get_card_from_node(current_node) == card:
			return True
		current_node = get_next_card_node(current_node)
	return False

# Determines if there are any cards in the hand.
# Return 0 if the hand is empty; 1 otherwise.
def is_hand_empty(hand):
	return hand['first_card'] is None ## Could also be num_cards_in_hand == 0

def print_card(card):
	print('{face} of {suit}'.format(face = card[0], suit = card[2]))

def print_hand(hand):
	print('====')
	cur_card_node = hand['first_card']
	while cur_card_node is not None:
		print_card(cur_card_node['payload'])
		cur_card_node = cur_card_node['next']
	print('====')

