from Player import Player


class HumanPlayer(Player):

    def hit_me(self, deck):
        self.cards.append(deck.get_next_card())
        return self.sum_cards()
