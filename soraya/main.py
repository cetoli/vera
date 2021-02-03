# vera.soraya.main.py
"http://supygirls.pythonanywhere.com"
from _spy.vitollino.main import Cena, Elemento, Texto, STYLE, INVENTARIO
STYLE["width"] = 1200
STYLE["height"] = "650px"
FLORESTA = "https://i.imgur.com/bfO1gCN.jpg"
MACACO = "https://i.imgur.com/dIBkMcG.png"
TEXTO_MACACO= "Estou perdido! Ajude-me a encontrar minha mãe por favor! Mas cuidado, a floresta é perigosa..."

class CenaProxy:
    def __init__(self, aqui=None):
        self.aqui = aqui
        self.floresta_faca = None
    def vai(self):
        from rachel.main import FlorestaBanana
        self.floresta_faca = FlorestaBanana(self.aqui)
        #self.floresta_faca.esquerda = self.aqui
        self.floresta_faca.vai()


class FlorestaMacaco:
    def __init__(self, floresta_inicio=0, vida=3):
        floresta_faca = CenaProxy()
        floresta_inicio = Cena(FLORESTA, direita=floresta_faca)
        self.floresta_inicio = floresta_inicio
        self.fala = Texto(self.floresta_inicio, TEXTO_MACACO)
        self.macaco = Elemento(MACACO, style=dict(left="700px", top="400px", width="100px"))
        self.macaco.entra(floresta_inicio)
        self.macaco.vai=self.falamacaco
        #floresta_inicio.vai()
        
    def vai(self):
        self.floresta_inicio.vai()
        
    def falamacaco(self,_):
        self.fala.vai() 
        
if __name__ == "__main__":
    INVENTARIO.inicia()
    a_floresta = FlorestaMacaco()
    a_floresta.vai()        
