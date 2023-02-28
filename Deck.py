from Card import Card
import random


class Deck:

    def __init__(self):
        self.cards = []
        self.create_deck()
        self.last_card = 0

    def create_deck(self):
        self.last_card = 0
        card_types = ['treboles', 'espadas', 'corazones', 'diamantes']
        for type in card_types:
            for number in range(1, 14):
                card = Card(number, type)
                self.cards.append(card)

    def show(self):
        for card in self.cards:
            card.show()

    def shuffle(self):
        for cel in range(len(self.cards)):
            r = random.randint(0, 51)
            temp = self.cards[cel]
            self.cards[cel] = self.cards[r]
            self.cards[r] = temp

    def get_next_card(self):
        card = self.cards[self.last_card]
        self.last_card += 1
        return card
