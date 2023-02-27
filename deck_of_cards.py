from random import shuffle


class Card:
    # Class to represent individual cards in the deck
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return "{} of {}".format(self.value, self.suit)


class Deck:
    # Class to represent the entire deck of cards
    def __init__(self):
        c_values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        c_suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        self.cards = [Card(value, suit) for suit in c_suits for value in c_values]

    def count(self):
        # Returns the count of remaining cards in the deck
        return len(self.cards)

    def __repr__(self):
        return "Deck of {} cards".format(self.count())

    def __iter__(self):
        return iter(self.cards)

    def _deal(self, amount):
        # Deals a specified amount of cards from the deck
        if self.count() == 0:
            raise ValueError("All cards have been dealt")
        dealt_cards = [self.cards.pop() for _ in range(min(self.count(), amount))]
        return dealt_cards

    def shuffle(self):
        # Shuffles the deck if it's a full deck
        if self.count() < 52:
            raise ValueError("Only full decks of cards can be shuffled")
        shuffle(self.cards)
        return self.cards

    def deal_card(self):
        # Deals a single card from the deck
        return self._deal(1)[0]

    def deal_hand(self, amount):
        # Deals a hand of specified amount of cards
        hand = self._deal(amount)
        return hand


# new_deck = Deck()
# new_deck.shuffle()
# print(new_deck.deal_hand(5))
# print(new_deck.count())
# print(new_deck.deal_card())
# print(new_deck.count())
# print(new_deck.deal_hand(5))
# print(new_deck.count())
# print(new_deck.deal_card())
# print(new_deck.count())