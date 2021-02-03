# vera.final.main.py
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
FLORESTA_FINAL = "https://i.imgur.com/rA40ylS.jpg"
MACACA_MAE = "https://i.imgur.com/mLv0OVD.png"

class CenaProxy:
    def __init__(self, aqui=None):
        self.aqui = aqui
        self.floresta_rio = None
    def vai(self):
        from rio.main import FlorestaRio
        self.floresta_rio = FlorestaRio(self.aqui)
        self.floresta_rio.esquerda = self.aqui
        self.floresta_rio.vai()


class Macaca:
    def __init__(self, aqui):
        self.aqui = aqui
        self.macaca = Elemento(MACACA_MAE, x=600, y=480, w=200, h=200)
        
    def vai(self):
        self.macaca.entra(self.aqui)
        Texto(self.aqui, "Você encontra a mãe do macaquinho e finaliza sua aventura! Parabéns!").vai()
        


class FlorestaFinal:
    def __init__(self, esquerda=None):
        # floresta_faca = FlorestaFaca() -XX- ERRO!
        self.floresta_inicio = None
        self.floresta_final = floresta_final = CenaProxy(self.floresta_inicio)
        esquerda = esquerda or floresta_final
        self.floresta_inicio = Cena(FLORESTA_FINAL, esquerda=esquerda)
        self.macaca_mae = Macaca(self.floresta_inicio)
        self.floresta_inicio.meio = self.floresta_inicio.direita = Macaca(self.floresta_inicio) 
        floresta_final.aqui = self.floresta_inicio 
        
    def vai(self):
        self.floresta_inicio.vai()
               
if __name__ == "__main__":
    INVENTARIO.inicia()
    a_floresta = FlorestaFinal()
    a_floresta.vai()