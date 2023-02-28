class Card:

    def __init__(self, number, type):
        self.type = type
        self.number = number

    def show(self):
        number = self.number_to_string()
        print(number, "de", self.type)

    def number_to_string(self):
        value = ""
        special_cards = {
            1:  "A",
            11: "J",
            12: "Q",
            13: "K"
        }
        value = str(self.number)

        if self.number in special_cards:
            value = special_cards[self.number]

        return value

    def get_number(self):
        return 10 if self.number > 10 else self.number

    def get_name_from_file(self):
        return "assets/Cards/"+self.number_to_string()+"_de_"+self.type.lower()+".png"
