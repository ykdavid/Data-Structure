from game_structures import *
import random

## Shuffle the cards.
def shuffle(deck):
	random.shuffle(deck)

## Given a deck and two hands, deal 5 cards to each hand.
## The first hand (p1_hand) gets the first card, the second
## hand gets the next, and alternate until each hand has
## the right number of cards.
def deal(deck, p1_hand, p2_hand):
	for i in range(NUM_CARDS_IN_HAND):
		add_card_to_hand(p1_hand,pop_card(deck))
		add_card_to_hand(p2_hand,pop_card(deck))

# If the player has a card of the same suit as the lead_card, they
# must play a card of the same suit.
# If the player does not have a card of the same suit, they can
# play any card.
def hand_has_suit(hand, suit):
	current_node = get_first_card_in_hand(hand)
	while current_node is not None:
		card = get_card_from_node(current_node) 
		if get_card_suit(card) == suit:
			return True
		current_node=get_next_card_node(current_node)
	return False

def is_legal_move(hand, lead_card, played_card):
    lead_suit = get_card_suit(lead_card)
    played_suit = get_card_suit(played_card)

    # 打印调试信息
    #print(f"Lead card: {lead_card}, Lead suit: {lead_suit}")
    #print(f"Played card: {played_card}, Played suit: {played_suit}")

    if hand_has_suit(hand, lead_suit):
        #print(f"Hand has {lead_suit}. Played suit: {played_suit}")
        return played_suit == lead_suit

    #print(f"Hand does not have {lead_suit}. Any card is legal.")
    return True

def get_card_suit(card):
    if card:
        return card[2]
    return None

def get_card_value(card):
    if card:
        return card[3]
    return None

## Return True if the followed card is not the same suit as the lead card,
##   unless the followed card is trump, and the lead card is NOT trump.
## If the cards are the same suit,
##   return True if the lead card is higher than the followed card
##   Return False if the lead card is lower than the followed card
def who_won(lead_card, followed_card, trump):
    lead_suit = get_card_suit(lead_card)
    followed_suit = get_card_suit(followed_card)
    lead_value = get_card_value(lead_card)
    followed_value = get_card_value(followed_card)

    # Debug prints to verify correctness of suits and values
    #print(f"Lead card: {lead_card}, Lead suit: {lead_suit}, Lead value: {lead_value}")
    #print(f"Followed card: {followed_card}, Followed suit: {followed_suit}, Followed value: {followed_value}")
    #print(f"Trump: {trump}")
    

    # Print comparison results for each condition
    if followed_suit == trump and lead_suit != trump:
        #print(f"Followed card {followed_card} wins (Trump is {trump}).")
        return False
    if lead_suit == trump and followed_suit != trump:
        #print(f"Lead card {lead_card} wins (Trump is {trump}).")
        return True
    if lead_value and followed_value:
        if lead_suit == followed_suit:
            result = lead_value > followed_value
            #print(f"Lead and followed cards have the same suit ({lead_suit}). Lead wins: {result}")
            return result

    # Default case
    #print(f"Lead card {lead_card} wins by default (No trump, different suits).")
    return True


# Given the player1 hand, play a card.
# Player 1 is always the computer.
# This function should choose a card from the hand,
# remove it from the hand, print out a message
# saying what card was played, and return the played card.
# I recommend beginning with choosing the card in a very simple
# manner: just remove/return the first card in the hand, regardless
# if it's a "good" card or not.
def take_player1_turn(hand, trump):
	played_card=get_card_from_hand(hand,0)
	#print(f"Player 1 (computer) played: {played_card[0]}")
	return played_card

# Given the player2 hand, play a card.
# Player 2 is always a human.
# This function should prompt the user to choose a card to play.
# It probably should print out the cards that are available to play.
# Once the human player chooses,
# remove it from the hand, print a message
# saying what card was played, and return the played card.
# This function does not have to enforce that a valid card is chosen.
def take_player2_turn(hand, trump):
	#print("Your hand:")
	#print_hand(hand)
	index = int(input("Choose a card to play (0 to 4): "))
	played_card = get_card_from_hand(hand, index)
	#print(f"Player 2 (human) played: {played_card[0]}")
	return played_card

# Take all the cards out of a given hand, and put them
# back into the deck.
def return_hand_to_deck(hand, deck):
	while not is_hand_empty(hand):
		card = get_card_from_hand(hand,0)
		push_card_to_deck(deck,card)


def swap_card_with_next(hand, index):
    # 獲取索引 index 和 index+1 處的節點
    card1_node = get_first_card_in_hand(hand)  # 從第一個節點開始
    for i in range(index):
        card1_node = get_next_card_node(card1_node)
    
    card2_node = get_next_card_node(card1_node)  # 下一個節點是 card1_node 的 next

    # 如果 card1_node 或 card2_node 不存在，則無法交換
    if card1_node is None or card2_node is None:
        #print(f"Cannot swap: card1_node or card2_node is None at index {index}")
        return

    # 保存原始的前後鏈接
    card1_prev = get_prev_card_node(card1_node)
    card2_next = get_next_card_node(card2_node)

    # 進行交換：card1_node 和 card2_node 交換
    set_next_card_node(card1_node, card2_next)
    set_prev_card_node(card2_node, card1_prev)

    # 更新前一個節點的 next，指向 card2_node
    if card1_prev is not None:
        set_next_card_node(card1_prev, card2_node)

    # 更新 card2_node 的 next 指向 card1_node
    set_next_card_node(card2_node, card1_node)
    set_prev_card_node(card1_node, card2_node)

    # 如果 card2_node 之後有節點，更新該節點的 prev，指向 card1_node
    if card2_next is not None:
        set_prev_card_node(card2_next, card1_node)

    # 如果 card1_node 是手牌的第一個節點，需要更新 hand 的 first_card
    if get_first_card_in_hand(hand) == card1_node:
        set_first_card_in_hand(hand, card2_node)

    # 打印除錯信息來確認交換後的結果
    #print(f"After swap - first_card: {get_card_from_node(get_first_card_in_hand(hand))}")

    
## Returns True if the value of this_card is greater than the value of that_card, accounting for trump
## True if this_card is trump and that_card is not
## True if this_card is the same suit of that_card, and the value of this_card is > than the value of that card
## True if that_card has a different suit than this_card
## True if that_card is None
def is_this_card_bigger_than_that_card(this_card, that_card, trump):
    this_suit = get_card_suit(this_card)
    that_suit = get_card_suit(that_card)

    # 如果 this_card 是王牌且 that_card 不是王牌，则 this_card 更大
    if this_suit == trump and that_suit != trump:
        return True

    # 如果 that_card 是王牌且 this_card 不是王牌，则 that_card 更大
    if that_suit == trump and this_suit != trump:
        return False

    # 如果两张牌的花色相同，则比较数值
    if this_suit == that_suit:
        return get_card_value(this_card) > get_card_value(that_card)

    # 如果两张牌花色不同且都不是王牌，可以根据某种自定义规则决定
    # 例如默认 this_card 更大，或者不交换它们
    return get_card_value(this_card) > get_card_value(that_card)  # 可以根据需求调整


# Sort the given hand in descending order of power.
# For full credit, implement your own sort algorithm (a Bubble Sort is easy with the Swap!).
#
# The sort order should be: all cards of the given trump suit should
# be the "highest", and A high down to 9;
# The other suits can be in random order, but the card values must go
# from high to low.
def sort_hand(hand, trump):
    """Sort the hand such that trump is first and everything else is in decreasing order"""
    
    n_cards = get_num_cards_in_hand(hand)  

    for i in range(n_cards - 1):
        for j in range(n_cards - 1 - i):
            current_card = get_card_from_hand_at_index(hand, j)
            next_card = get_card_from_hand_at_index(hand, j + 1)

            if current_card is None or next_card is None:
                print(f"Error: One of the cards is None at index {j}")
                continue

            if not is_this_card_bigger_than_that_card(current_card, next_card, trump):
                swap_card_with_next(hand, j)

