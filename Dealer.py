from Deck import Deck
from Player import Player
from VirtualPlayer import VirtualPlayer


class Dealer:
    def __init__(self, players):
        self.players = players
        self.results = []
        self.deck = Deck()

    def deal_cards(self):
        for player in self.players:
            cards = [self.deck.get_next_card(), self.deck.get_next_card()]
            player.assign_cards(cards)

    def start_game(self):
        self.deck.shuffle()
        self.deal_cards()
        return {
            "player": self.players[0].cards,
            "pc": self.players[1].cards
        }

    def who_won(self):
        won = 0
        value = 21

        for i in range(len(self.players)):
            sum = self.players[i].sum_cards()
            result = 21 - sum
            if result < value and result >= 0:
                value = result
                won = i

        return won == 0
