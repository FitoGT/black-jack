from tkinter import *
from Dealer import Dealer
from HumanPlayer import HumanPlayer
from VirtualPlayer import VirtualPlayer


class GameInterface:
    
    def __init__(self):
        self.window = Tk()
        self.window.geometry('1200x600')
        self.canvas = Canvas(self.window, width=1200, height=600)
        self.canvas.pack()
        self.startBtn = Button(self.window, text="Start Game", command=self.play)
        self.hitMeBtn = Button(self.window, text="Hit Me!", command=self.hit_me)
        self.stayBtn = Button(self.window, text="Stay!", command=self.end_game)
        self.won_label = Label(self.window, text="", background="Green", foreground="White", font="arial 15 bold")
        self.won_label.place(x=50, y=280)
        self.draw_bkg()
        self.draw_labels()
        self.hide_game_options()

        self.player = HumanPlayer('Jugador 1')
        self.pc = VirtualPlayer('Computadora 1')
        self.dealer = Dealer([self.player, self.pc])
        self.window.mainloop()
    
    def play(self):
        self.draw_bkg()
        self.won_label.config(text="")
        self.pc_x = 110
        self.pc_y = 143
        self.player_x = 110
        self.player_y = 490
        self.pc_start = self.pc_x
        cards = self.dealer.start_game()
        self.pc.play(self.dealer.deck)
        self.pc_x = self.inital_state(cards["pc"], self.pc_x, self.pc_y, True)
        self.player_x = self.inital_state(cards["player"], self.player_x, self.player_y)
        self.show_game_options()

    def hit_me(self):
        sum = self.player.hit_me(self.dealer.deck)
        if sum > 21:
            self.end_game()
        
        self.draw_rectangles(1, self.player_x-60, 400, 120, 175, 0)
        self.draw_card(self.player_x, self.player_y, self.player.cards[-1].get_name_from_file())
        self.player_x += 125
    
    def end_game(self):
        self.draw_rectangles(1, self.pc_start-60, self.pc_y-88, 120, 175, 0)
        self.draw_card(self.pc_start, self.pc_y, self.pc.cards[0].get_name_from_file())

        player_won = self.dealer.who_won()
        
        if player_won:
            self.won_label.config(text="You Win")
        
        else:
            self.won_label.config(text="You Lose")
        self.hide_game_options()

    def inital_state(self, cards, x, y, hide_first=False):
        for i in range(len(cards)):
            self.draw_rectangles(1, x-60, y-88, 120, 175, 5)
            name = 'assets/Cards/_s.png' if hide_first and i==0 else cards[i].get_name_from_file()
            self.draw_card(x, y, name)
            x += 125
        return x
    
    def show_game_options(self):
        self.hitMeBtn.place(x=700, y=500)
        self.stayBtn.place(x=700, y=550)
        self.startBtn.place_forget()
        
    def hide_game_options(self):
        self.hitMeBtn.place_forget()
        self.stayBtn.place_forget()
        self.startBtn.place(x=400, y=300)
    
    def draw_bkg(self):
        bkg = PhotoImage(file="assets/fondo.png")
        img = Label(image=bkg)
        img.image = bkg
        
        self.canvas.create_image(300,200, image=bkg)
        self.canvas.create_image(300,400, image=bkg)
        self.canvas.create_image(900,200, image=bkg)
        self.canvas.create_image(900,400, image=bkg)

        arr = PhotoImage(file="assets/adornos.png")
        img = Label(image=arr)
        arr = arr.subsample(7)
        img.image = arr

        self.canvas.create_image(980,460, image=arr)

    def draw_card(self, x, y, image):
        img = PhotoImage(file=image)
        img = img.subsample(2)
        label = Label(image=img)
        label.image = img
        self.canvas.create_image(x, y, image=img)

    def draw_polygon(self, x, y, **args):
        dots = []
        for i in range(len(x)):
            dots.append(x[i])
            dots.append(y[i])
        dots.append(x[0])  
        dots.append(y[0])
        return self.canvas.create_polygon(dots,**args) 
        
    def draw_rectangles(self, count, xStart, yStart, xSize, ySize, margin=10):
        for i in range(count):
            self.draw_polygon([xStart, xStart+xSize,xStart+xSize, xStart], 
                              [yStart, yStart, yStart+ySize, yStart+ySize],
                              fill="#FFFFFF", width=2, outline="#000000")
            xStart = xStart + xSize + margin

    def draw_labels(self):
        label = Label(self.window, text="Compu 1", background="Green", foreground="White", font="arial 15 bold")
        label.place(x=50, y=20)
        label = Label(self.window, text="Jugador 1", background="Green", foreground="White", font="arial 15 bold")
        label.place(x=50, y=360)
        


def main():
    g = GameInterface()
if __name__ == '__main__':
    main()
    