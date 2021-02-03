# vera.amanda.main.py
"http://supygirls.pythonanywhere.com"
from _spy.vitollino.main import Cena, Texto, INVENTARIO, STYLE
from elemento.main import Elemento
# from morgan.main import FlorestaLeao
STYLE["width"], STYLE["height"] = 1400, "650px"
FLORESTA = "https://i.imgur.com/vlJS7Ry.jpg"

ANTIDOTO = "https://imgur.com/xkFpBsx.png"
ANTIDOTE = "https://imgur.com/GYPNVGN.png"
FACA = "https://i.imgur.com/H2vMcB4.png"
TEXTO_FACA= "A faca está afiada, me cortei! Faca perigosa, melhor chutar para longe"
FACA_FOI= "Ainda bem que me livrei daquela coisa perigosa!"
TEXTO_FACA= "A faca está afiada, me cortei! Faca perigosa, melhor pegar com cuidado"
FACA_FOI= "Cuidadosamente, você coloca a faca na bolsa!"
FACA_USA= "Você segura a faca na mão!"
LEAO = "https://i.imgur.com/4gXpvfQ.png"
LANTERNA = "https://i.imgur.com/OO5pLxV.png"
CAPA_DE_CHUVA = "https://i.imgur.com/09U7IBK.png"
CORDA = "https://i.imgur.com/lCWG2Co.png"


class CenaProxy:
    def __init__(self, aqui=None):
        self.aqui = aqui
        self.floresta_leao = None
    def vai(self):
        from morgan.main import FlorestaLeao
        self.floresta_leao = FlorestaLeao(self.aqui)
        # self.floresta_leao.esquerda = self.aqui
        self.floresta_leao.vai()


class Faca:
    def __init__(self, floresta_inicio):
        self.floresta_inicio = floresta_inicio
        self.fala = Texto(self.floresta_inicio, TEXTO_FACA)
        self.falou = Texto(self.floresta_inicio, FACA_FOI)
        self.usar = Texto(self.floresta_inicio, FACA_USA)
        # self.faca = Elemento(FACA, style=dict(left="200px", width="80px"), vai=self.pega)
        drag = dict(faca=lambda *_: self.fala.vai())
        self.faca = Elemento(FACA, tit="faca", x=600, y=500, w=80, vai=self.pega)
        # self.leao = Elemento(LEAO, tit="leao", x=800, y=500, w=180, drop=drag, cena=floresta_inicio)
        self.longe = Cena()
        self.na_mao = False
        self.faca.entra(self.floresta_inicio)
    
    def pega(self, _):
        INVENTARIO.bota(self.faca)
        self.faca.do_drag(True)
        #self.fala.vai()
        self.faca.vai = self.guarda
    
    def guarda(self, _):
        INVENTARIO.bota(self.faca)
        self.falou.vai()
        self.faca.vai = self.usa
    
    def chuta(self, _):
        self.faca.entra(self.longe)
        self.falou.vai()
    
    def usa(self, _):
        self.na_mao = True
        self.usar.vai()
        
        
        
class FlorestaFaca:
    def __init__(self, esquerda=None):
        # floresta_leao = FlorestaLeao() -XX- ERRO!
        self.floresta_inicio = None
        floresta_leao = CenaProxy(self.floresta_inicio)
        esquerda = esquerda or floresta_leao
        self.floresta_inicio = Cena(FLORESTA, esquerda=esquerda, direita=floresta_leao)
        floresta_leao.aqui = self.floresta_inicio
        faca = Faca(self.floresta_inicio)
        self.lanterna = Elemento (LANTERNA,tit="lanterna", drag=True, cena = self.floresta_inicio, x=300, y=500, vai=self.guarda)
        self.capa_de_chuva = Elemento (CAPA_DE_CHUVA, tit="capa de chuva", drag=True, cena = self.floresta_inicio, x=200, y=300, vai=self.guardacapa)
        self.corda = Elemento (CORDA, tit="corda", drag=True, cena = self.floresta_inicio, x=850, y=350, vai=self.guardacorda)
        self.antidoto = Elemento(ANTIDOTE, tit="antidoto", drag=True, cena = self.floresta_inicio, x=700, y=480, w=80, vai=self.pegaant)
        
    def pegaant(self, _):
        INVENTARIO.bota(self.antidoto)
        
    def guarda(self, _):
        INVENTARIO.bota(self.lanterna)
        
    def guardacapa(self, _):
        INVENTARIO.bota(self.capa_de_chuva)
        
    def guardacorda(self, _):
        INVENTARIO.bota(self.corda)
        
    def vai(self):
        self.floresta_inicio.vai()
        
if __name__ == "__main__":
    INVENTARIO.inicia()
    a_floresta = FlorestaFaca()
    a_floresta.vai()