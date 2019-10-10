# vera.chuva.main.py
# vera.rachel.main.py
"http://supygirls.pythonanywhere.com"
from _spy.vitollino.main import Cena, Texto, INVENTARIO, STYLE
from elemento.main import Elemento
from cobra.main import Cobra
CHUVA = "https://i.imgur.com/ubkw6wx.jpg"
STYLE["width"] = 1400
STYLE["height"] = "650px"
# from amanda.main import FlorestaFaca
FLORESTA = "https://i.imgur.com/VHaolvA.jpg"
BANANA = "https://i.imgur.com/HnIHJd7.png"
TEXTO_BANANA= "O macaquinho pode ficar com fome! Coloque na bolsa!"
BANANA_FOI= "Hummm, que delícia!"
BANANA_USA= "Você segura a banana na mão!"
REDE = "https://i.imgur.com/9Fig2oH.png"
TEXTO_REDE= "Caí na armadilha! Pegue a faca para cortá-la!"
COBRA = "https://i.imgur.com/nQ0StLK.png"
BISCOITO = "https://i.imgur.com/ywr5b2D.png"
CAVERNA = "https://i.imgur.com/00MjS1k.jpg"
LANTERNA = "https://i.imgur.com/OO5pLxV.png"
INTERIOR_CAVERNA = "https://i.imgur.com/lNPYjUA.jpg"
FLORESTA_CHUVA = "https://i.imgur.com/sDQ5r36.jpg"
CAPA_DE_CHUVA = "https://i.imgur.com/09U7IBK.png"
RIO = "https://i.imgur.com/uYrWcA2.jpg"
CORDA = "https://i.imgur.com/lCWG2Co.png"

class CenaProxy:
    def __init__(self, aqui=None):
        self.aqui = aqui
        self.floresta_faca = None
    def vai(self):
        from amanda.main import FlorestaFaca
        self.floresta_faca = FlorestaFaca(self.aqui)
        self.floresta_faca.esquerda = self.aqui
        self.floresta_faca.vai()


    def pega(self, *_):
        self.rede.entra(self.floresta_inicio)
        self.fala.vai()
        
    def corta(self, *_):
        self.rede.entra(self.longe)


class Molhado:
    def __init__(self, aqui):
        self.aqui = aqui
        
    def vai(self):
        Texto(self.aqui, "Você fica muito molhado e não consegue continuar").vai()


class FlorestaChuva:
    def __init__(self, esquerda=None):
        # floresta_faca = FlorestaFaca() -XX- ERRO!
        self.floresta_inicio = None
        floresta_faca = CenaProxy(self.floresta_inicio)
        esquerda = esquerda or floresta_faca
        self.floresta_inicio = Cena(FLORESTA_CHUVA, esquerda=esquerda)
        self.floresta_inicio.meio = self.floresta_inicio.direita = Molhado(self.floresta_inicio) 
        floresta_faca.aqui = self.floresta_inicio 
        
    def vai(self):
        if "capa de chuva" in INVENTARIO.item:
        self.floresta_inicio.vai()
        Texto(self.aqui, "Você se protege").vai()
               
if __name__ == "__main__":
    INVENTARIO.inicia()
    a_floresta = FlorestaChuva()
    a_floresta.vai()