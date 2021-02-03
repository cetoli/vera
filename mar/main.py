# vera.mar.main.py
from _spy.vitollino.main import Cena, STYLE, Texto
STYLE["width"], STYLE["height"] = 1200, "650px"
from elemento.main import Elemento
PRAIA = "https://i.imgur.com/slKTEBc.png"
ILHAMAR = "https://i.imgur.com/3FUDzbn.jpg"
BARCO = "https://i.imgur.com/ckjd6cI.png"
BOIA = "https://i.imgur.com/GmzOUTL.png"
ilhamar = Cena(ILHAMAR)
def vai_trilha(*_):
    from trilhacaverna.main import Caverna
    Caverna().vai()
praia = Elemento(PRAIA, cena=ilhamar, x=700, y=398, h=900, style=dict(width= 500, height="650px"),
vai=vai_trilha)
Texto(ilhamar, "mimi").vai()
ilhamar.vai()
def vai_fundo(*_):
    from perigo1.main import Perigo
    Perigo().vai()


barco = Elemento(BARCO, cena=ilhamar, x=70, y=430, h=500, style=dict(width= 80, height="650px"), vai=vai_fundo)
boia = Elemento(BOIA, cena=ilhamar, x=30, y=440, h=900, style=dict(width= 30, height="650px"))
boia2 = Elemento(BOIA, cena=ilhamar, x=100, y=500, h=900, style=dict(width= 30, height="650px"))
boia3 = Elemento(BOIA, cena=ilhamar, x=200, y=550, h=900, style=dict(width= 30, height="650px"))
boia4 = Elemento(BOIA, cena=ilhamar, x=320, y=600, h=900, style=dict(width= 30, height="650px"))
boia5 = Elemento(BOIA, cena=ilhamar, x=440, y=620, h=900, style=dict(width= 30, height="650px"))
boia6 = Elemento(BOIA, cena=ilhamar, x=150, y=450, h=900, style=dict(width= 30, height="650px"))
boia7 = Elemento(BOIA, cena=ilhamar, x=300, y=490, h=900, style=dict(width= 30, height="650px"))
boia8 = Elemento(BOIA, cena=ilhamar, x=450, y=530, h=900, style=dict(width= 30, height="650px"))
boia9 = Elemento(BOIA, cena=ilhamar, x=600, y=570, h=900, style=dict(width= 30, height="650px"))
boia10 = Elemento(BOIA, cena=ilhamar, x=750, y=600, h=900, style=dict(width= 30, height="650px"))