# vera.morgan.main.py
"http://supygirls.pythonanywhere.com"
from _spy.vitollino.main import Cena, Elemento, Texto, INVENTARIO, STYLE
# from morgan.main import FlorestaBanana
from elemento.main import Elemento as Elem
STYLE["width"], STYLE["height"] = 1400, "650px"
FLORESTA = "https://i.imgur.com/vlJS7Ry.jpg"
BANANA = "https://i.imgur.com/HnIHJd7.png"
TEXTO_LEAO= "O leão está com fome, tome cuidado ele pode comer você!"
LEAO_COME= "Você morreu!"
MORDIDA = "https://i.imgur.com/EOHbtUB.png"




class CenaProxyCobra:
    def __init__(self, aqui=None):
        self.aqui = aqui
        self.floresta_macaco = None
    def vai(self, *_):
        from cobra.main import FlorestaCobra
        self.floresta_cobra = FlorestaCobra()
        #self.aqui.esquerda = self.aqui.meio = self.aqui.direita = self.aqui.mordida.vai = self.floresta_macaco
        self.floresta_cobra.vai()



class CenaProxy:
    def __init__(self, aqui=None):
        self.aqui = aqui
        self.floresta_macaco = None
    def vai(self, *_):
        from soraya.main import FlorestaMacaco
        self.floresta_macaco = FlorestaMacaco(vida=2)
        #self.aqui.esquerda = self.aqui.meio = self.aqui.direita = self.aqui.mordida.vai = self.floresta_macaco
        self.floresta_macaco.vai()

FLORESTA = "https://i.imgur.com/wBw3Lyl.jpg"
LEAO = "https://i.imgur.com/4gXpvfQ.png"


class Leao:
    def __init__(self, floresta_inicio):
        self.floresta_inicio = floresta_inicio
        self.fala = Texto(self.floresta_inicio, TEXTO_LEAO)
        self.falou = Texto(self.floresta_inicio, LEAO_COME)
        #self.leao = Elemento(LEAO, style=dict(left="150px",width="200px", top="480px"), vai=self.pega)
        self.leao = Elemento(LEAO, x=150, y=400, w=200, h=200, vai=self.pega)
        self.morreu = Cena()
        self.comeu = False
        self.leao.entra(self.floresta_inicio)
        self.leao.vai=self.falaleaofome
        self.mordida = Elem(MORDIDA, x=0, y=0, w=1400, h=650, style={"opacity": 0.5}, tipo="100% 100%") #, vai=self.antidoto)
        
    def vai(self):
        self.floresta_inicio.vai()
        
    def falaleaofome(self,_):
        self.leao.vai=self.falaleaocome
        self.fala.vai()   
        
    def falaleaocome(self,_):
        self.mordida.entra(self.floresta_inicio)
        self.mordida.vai = CenaProxy(self.floresta_inicio).vai
        self.falou.vai()
        
    def pega(self, _): 
        self.fala.vai()
        self.leao.vai = self.foto

          
    def usa(self, _): 
        self.comeu = True
        self.falou.vai()
    
    def morre(self, _): 
        self.usar.vai()
        
class FlorestaLeao:
    def __init__(self, esquerda=None):
        self.floresta_inicio = None
        floresta_banana = CenaProxyCobra(self.floresta_inicio)
        esquerda = esquerda or floresta_banana
        self.floresta_inicio = Cena(FLORESTA, esquerda=esquerda, direita=floresta_banana)
        leao = Leao(self.floresta_inicio)
        
        
        
    def vai(self):
        self.floresta_inicio.vai()

if __name__ == "__main__":

    
    a_floresta = FlorestaLeao()
    a_floresta.vai()

