# vera.cavernaamigo.main.py
from _spy.vitollino.main import Cena, STYLE
STYLE["width"], STYLE["height"] = 1200, "650px"
from elemento.main import Elemento
CAVERNAAMIGO = "https://i.imgur.com/rHNPcSh.jpg"
AMIGO = "https://i.imgur.com/T9EbLID.png"
GRADE = "https://i.imgur.com/B8tB6cK.png"
CADEADO = "https://i.imgur.com/4qa6rC6.png"
ESMERALDA = "https://i.imgur.com/4JB2tXA.png"
cavernaamigo = Cena(CAVERNAAMIGO)
class Prisao:
    def __init__(self):
        ativa = dict(chave=self.abre)
        amigo = Elemento (AMIGO, cena = cavernaamigo, x= 600, y= 320, w= 200, h= 200)
        self.grade = Elemento (GRADE, cena = cavernaamigo, x= 510, y= 240, w= 300, h= 300)
        self.cadeado = Elemento (CADEADO, cena = cavernaamigo, drop=ativa, x= 510, y= 240, w= 50, h= 50)
        self.esmeralda = Elemento (ESMERALDA, x= 100, y= 200, w= 100, h= 150)
        
    def abre(self, *_):
        limbo = Cena()
        self.grade.entra(limbo)
        self.cadeado.entra(limbo)
        self.esmeralda.entra(cavernaamigo)
        
Prisao()

if __name__ == "__main__":
    cavernaamigo.vai()
    



    
