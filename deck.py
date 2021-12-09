'''For The game blackjack '''

def card_name(card_rank):
    '''Returns the given card's official name.
    Args:
        card_rank: The numeric representation of a card.
    Returns:
        A string representing the official name of the given card.
    Examples:
        card_name(2) returns "2"
        card_name(11) returns "Jack"
    '''
    if card_rank == 1:
        card_rank = "Ace"
    elif card_rank == 11:
        card_rank = "Jack"
    elif card_rank == 12:
        card_rank = "Queen"
    elif card_rank == 13:
        card_rank = "King"
    else:
        card_rank = str(card_rank)
    return card_rank
def card_value(card_rank):
    '''Returns the given card's value.
    Args:
        card_rank: The numeric representation of a card.
    Returns:
        The face value of the card, except for Ace, Jack, Queen, and King.
    Examples:
         card_value(1) returns 11 for Ace, card_value(4) returns 4 for 4
    '''
    if 11 <= card_rank <= 13:
        card_rank = 10
    elif card_rank == 1:
        card_rank = 11
    else:
        card_rank = int(card_rank)
    return card_rank
def end_turn_status(hand):
    '''Returns the status at the end of a player's turn.
    Args:
        hand: The sum of of all the cards in the hand.
    Returns:
        '', 'BLACKJACK!', or 'BUST.', depending on the value of the given hand.
    Examples:
         if hand is less than 21:'', if hand is equal to 21:'BLACKJACK!'
    '''
    if hand > 21:
        hand = "BUST."
    elif hand == 21:
        hand = "BLACKJACK!"
    else:
        hand = ""
    return hand
def end_game_status(user_hand, dealer_hand):
    '''Prints the winner based on the final hands.
    Args:
        user_hand:Total card in the user's hand, dealer_hand: Total cards in the dealer's hand.
    Returns:
        'You win!', 'Dealer wins!', or 'Tie.', depending on the values of the given hands.
    Examples:
        if user_hand beats dealer_hand:'You win!'
    '''
    if user_hand <= 21 < dealer_hand:
        hand = "You win!"
    elif dealer_hand <= 21 < user_hand:
        hand = "Dealer wins!"
    elif  dealer_hand < user_hand <= 21:
        hand = "You win!"
    elif user_hand < dealer_hand <= 21:
        hand = "Dealer wins!"
    else:
        hand = "Tie."
    return hand
    