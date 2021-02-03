# vera.trilhacaverna.main.py
from _spy.vitollino.main import Cena, STYLE, INVENTARIO
STYLE["width"], STYLE["height"] = 1200, "650px"
from elemento.main import Elemento
from cavernatesouro.main import Tesouro
from cavernaamigo.main import cavernaamigo
TRILHACAVERNA = "https://i.imgur.com/bNEzuBs.jpg"
ARANHA = "https://i.imgur.com/xXPifks.png"
COBRA = "https://i.imgur.com/EoIRfsD.png"
SETADIREITA = "https://i.imgur.com/HiCksFh.png"
SETAESQUERDA = "https://i.imgur.com/zpPeaMk.png"
CHAVE = "https://i.imgur.com/O3oqeU0.png"
class Caverna:
    def __init__(self):
        self.trilha = trilhacaverna = Cena(TRILHACAVERNA)
        INVENTARIO.inicia()
        #trilhacaverna.vai()
        aranha = Elemento (ARANHA, cena = trilhacaverna, x= 400, y= 150, w= 200, h= 200)
        cobra = Elemento (COBRA, cena = trilhacaverna, x= 800, y= 450, w= 400, h= 200)
        setadireita = Elemento (SETADIREITA, cena = trilhacaverna, x= 1100, y= 450, w= 200, h= 100)
        setaesquerda = Elemento (SETAESQUERDA, cena = trilhacaverna, x= 30, y= 480, w= 100, h= 100)
        setadireita.vai = self.dir_vai
        setaesquerda.vai = cavernaamigo.vai
        chave = Elemento (CHAVE, cena = trilhacaverna, tit="chave", drag = True,  x= 500, y= 450, w= 100, h= 50)
        chave.vai = lambda *_: INVENTARIO.bota(chave)
    def vai(self, *_):
        self.trilha.vai()
    def dir_vai(self, *_):
        from cavernatesouro.main import Tesouro
        Tesouro().vai()


if __name__ == "__main__":
    Caverna().vai()

