class Interface:

    def get_real_number(self, title):
        var = input(title)
        number = 0
        try:
            number = float(var)
        except ValueError as error:
            print('Data is not a number', error)
        return number

    def get_int_number(self, title):
        var = input(title)
        number = 0
        try:
            number = float(var)
        except ValueError as error:
            print('Data is not a number', error)
        return number
