import unittest

from deck_of_cards import Card, Deck


class CardTests(unittest.TestCase):
    def setUp(self):
        self.card = Card("A", "Hearts")

    def test_init(self):
        """cards should have suit and value"""
        self.assertEqual(self.card.suit, "Hearts")
        self.assertEqual(self.card.value, "A")

    def test_repr(self):
        """repr should return a string of the form VALUE of SUIT"""
        self.assertEqual(repr(self.card), 'A of Hearts')

class DeckTests(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()

    def test_init(self):
        """decks should have a cards attr, which is a list"""
        self.assertTrue(isinstance(self.deck.cards, list))
        self.assertEqual(len(self.deck.cards), 52)

    def test_repr(self):
        """repr should return a string of the form 'Deck of 52 cards'"""
        self.assertEqual(repr(self.deck), "Deck of 52 cards")

    def test_count(self):
        self.assertEqual(self.deck.count(), 52)
        self.deck.cards.pop()
        self.assertEqual(self.deck.count(), 51)

    def test_deal_sufficient_cards(self):
        cards = self.deck._deal(10)
        self.assertEqual(len(cards), 10)
        self.assertEqual(self.deck.count(), 42)

    def test_deal_insufficient_cards(self):
        cards = self.deck._deal(100)
        self.assertEqual(len(cards), 52)
        self.assertEqual(self.deck.count(), 0)

    def test_deal_no_cards(self):
        self.deck._deal(self.deck.count())
        with self.assertRaises(ValueError):
            self.deck._deal(1)

    def test_deal_cards(self):
        card = self.deck.cards[-1]
        dealt_card = self.deck.deal_card()
        self.assertEqual(card, dealt_card)
        self.assertEqual(self.deck.count(), 51)

    def test_deal_hand(self):
        cards = self.deck._deal(20)
        self.assertEqual(len(cards), 20)
        self.assertEqual(self.deck.count(), 32)

    def test_shuffle_full_deck(self):
        cards = self.deck.cards[:]
        self.deck.shuffle()
        self.assertNotEqual(cards, self.deck.cards)
        self.assertEqual(self.deck.count(), 52)

    def test_shuffle_not_full_deck(self):
        self.deck._deal(1)
        with self.assertRaises(ValueError):
            self.deck.shuffle()


if __name__ == "__main__":
    unittest.main()
