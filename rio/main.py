# vera.rio.main.py
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
        from final.main import FlorestaFinal
        self.floresta_final = FlorestaFinal(self.aqui)
        self.floresta_final.esquerda = self.aqui
        self.floresta_final.vai()


class Molhado:
    def __init__(self, aqui):
        self.aqui = aqui
        
    def vai(self):
        Texto(self.aqui, "Você tem medo de se afogar e não consegue continuar").vai()


class FlorestaRio:
    def __init__(self, esquerda=None):
        # floresta_faca = FlorestaFaca() -XX- ERRO!
        self.floresta_inicio = None
        self.floresta_final = floresta_final = CenaProxy(self.floresta_inicio)
        esquerda = esquerda or floresta_rio
        self.floresta_inicio = Cena(RIO, esquerda=esquerda)
        self.floresta_inicio.meio = self.floresta_inicio.direita = Molhado(self.floresta_inicio) 
        floresta_final.aqui = self.floresta_inicio 
        
    def vai(self):
        if "corda" in INVENTARIO.item:
            INVENTARIO.item["corda"].vai = self.pendura
        self.floresta_inicio.vai()
        
    def pendura(self, _):
        Texto(self.floresta_inicio, "Você se pendura na corda e se balança para atravessar o rio").vai()
        self.floresta_inicio.direita = self.floresta_final
        self.floresta_inicio.meio = self.floresta_final
               
if __name__ == "__main__":
    INVENTARIO.inicia()
    a_floresta = FlorestaRio()
    a_floresta.vai()