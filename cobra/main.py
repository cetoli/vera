# vera.cobra.main.py
# vera.rachel.main.py
"http://supygirls.pythonanywhere.com"
from _spy.vitollino.main import Cena, Elemento, Texto, INVENTARIO, STYLE
from elemento.main import Elemento as Elem
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
TEXTO_COBRA = "Fui picado! Preciso do antídoto!"
MORDIDA = "https://i.imgur.com/EOHbtUB.png"

class CenaProxy:
    def __init__(self, aqui=None):
        self.aqui = aqui
        self.caverna = None
    def vai(self):
        from caverna.main import Caverna
        self.caverna = Caverna()
        self.caverna.esquerda = self.aqui
        self.caverna.vai()


class Cobra:
    def __init__(self, floresta_inicio):
        self.floresta_inicio = floresta_inicio
        self.fala = Texto(self.floresta_inicio, TEXTO_COBRA)
        self.cobra = Elemento(COBRA, style=dict(left="800px", top="400px", width="150px"))
        if "antidoto" in INVENTARIO.item:
            INVENTARIO.item["antidoto"].vai = self.antidoto 
        self.cobra.entra(floresta_inicio)
        self.cobra.vai=self.falacobra
        self.mordida = Elem(MORDIDA, x=0, y=0, w=1400, h=650, style={"opacity": 0.5}, tipo="100% 100%") #, vai=self.antidoto)
        
    def vai(self):
        self.floresta_inicio.vai()
        
    def falacobra(self,_):
        self.mordida.entra(self.floresta_inicio)
        self.fala.vai()
        
    def antidoto(self,_):
        self.mordida.entra(Cena())
        Texto(self.floresta_inicio, "Você toma o antídoto e fica curado").vai()
        
class FlorestaCobra:
    def __init__(self):
        # floresta_faca = FlorestaFaca() -XX- ERRO!
        self.floresta_inicio = None
        floresta_direita = CenaProxy(self.floresta_inicio)
        self.floresta_inicio = Cena(FLORESTA, direita=floresta_direita)
        # banana = Banana(self.floresta_inicio)
        # rede = Rede(self.floresta_inicio)
        cobra = Cobra(self.floresta_inicio)
        
    def vai(self):
        self.floresta_inicio.vai()
                
if __name__ == "__main__":
    INVENTARIO.inicia()
    a_floresta = FlorestaCobra()
    a_floresta.vai()