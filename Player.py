class Player:
    def __init__(self, name, cards=[]):
        self.name = name
        self.cards = cards

    def assign_cards(self, cards):
        self.cards = cards

    def show_cards(self):
        print(self.name, "estas son tus cartas:")
        for card in self.cards:
            card.show()
        print("Suma:", self.sum_cards())

    def sum_cards(self):
        sum = 0
        aces = 0

        for card in self.cards:
            value = card.get_number()
            if value == 1:
                aces += 1
            sum += value

        if aces > 0 and sum + 10 <= 21:
            sum += 10

        return sum
