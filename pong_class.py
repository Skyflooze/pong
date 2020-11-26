class Raquette:
    
    def __init__(self, direction):
        self.bx = 4
        self.by = 4
        self.corps = []
        self._direction = direction

    def set_direction(self,val):
        self._direction = val

    def get_direction(self):
        return self._direction

    direction = property(get_direction, set_direction)

    def apparence(self):
        self.forme = ([(6,125),(11,125),(6,175),(11,175)],[(497,125),(492,125),(497,175),(492,175)])

    def remplir_corps(self):
        self.cd=0
        self.corps = [
            [(apparence[0][0]*self.step+self.cd[0]),(apparence[0][1]*self.step+self.cd[1])]]

class Game:
    def __init__(self,step):
        self.step = step
'''
class Game:

    def init(self):
        self.interface()
        self.scorej1 = 0
        self.scorej2 = 0
        self.largeur = 500
        self.hauteur = 300

    def interface(self):
        self.root = Tk()
        self.text = Text(self.root)
        self.canvas = Canvas(self.root, width=self.largeur, height=self.hauteur, background="black")
        self.raquette1 = self.canvas.create_rectangle(6, 125,  11, 200, width=1, fill="white", outline="")
        self.raquette2 = self.canvas.create_rectangle(497, 125, 492, 200, width=1, fill="white", outline="")
        self.balle = self.canvas.create_oval(240,120,260,140,fill='white')
        self.bordHaut = self.canvas.create_rectangle(0, 0, 503, 10, fill='green')
        self.bordBas = self.canvas.create_rectangle(0, 292, 503, 302, fill='green')

    def est_mort(self):
        self.canvas.delete(ALL)
        self.text.insert(INSERT, "GAME OVER")
        self.text.pack()
        self.text.insert(INSERT, f"Score du joueur 1 : {self.scorej1}\nScore du joueur 2 : {self.scorej2}")
'''
