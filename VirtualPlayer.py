from Player import Player


class VirtualPlayer(Player):

    def play(self, deck):
        while(self.sum_cards() < 16):
            self.cards.append(deck.get_next_card())
        return self.sum_cards()
