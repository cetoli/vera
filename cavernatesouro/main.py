# vera.cavernatesouro.main.py
from _spy.vitollino.main import Cena, STYLE, Codigo, Texto
STYLE["width"], STYLE["height"] = 1200, "650px"
from elemento.main import Elemento
CAVERNATESOURO = "https://i.imgur.com/RgatDJ4.jpg"
TESOURO = "https://i.imgur.com/8YK3cfO.png"
class Tesouro:
    def __init__(self):
        self.cavernatesouro = cavernatesouro = Cena(CAVERNATESOURO)
        codigo = Codigo ("", "",cena = cavernatesouro, style = dict( x= 400, y= 300))
        tesouro = Elemento (TESOURO, x= 245, y= 200, w= 700, h= 400)
        tesouro.vai = lambda *_: tesouro.entra(cavernatesouro)
        def troca(*_):
            cavernatesouro.meio = tesouro
        codigo = Texto (cavernatesouro, "Opa!! Você achou o tesouro!!",
        "Mas, cuidado: ao decidir pegar o tesouro, seu amigo não poderá ser salvo",
        style = dict( x= 400, y= 300), foi=troca)
        cavernatesouro.meio = codigo
        
    def vai(self, *_):
        self.cavernatesouro.vai()

if __name__ == "__main__":
    Tesouro.vai()
    
