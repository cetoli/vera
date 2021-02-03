# vera.caverna.main.py
# vera.rachel.main.py
"http://supygirls.pythonanywhere.com"
from _spy.vitollino.main import Cena, Texto, INVENTARIO, STYLE, Elemento
#from elemento.main import Elemento
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
TEXTO_CAVERNA = "Está muito escuro...não consigo enxergar!"
LANTERNA = "https://i.imgur.com/OO5pLxV.png"
FLORESTA_CHUVA = "https://i.imgur.com/sDQ5r36.jpg"
CAPA_DE_CHUVA = "https://i.imgur.com/09U7IBK.png"
RIO = "https://i.imgur.com/uYrWcA2.jpg"
CORDA = "https://i.imgur.com/lCWG2Co.png"
ENTRADA = "https://i.imgur.com/6e096Va.png"

class CenaProxy:
    def __init__(self, aqui=None):
        self.aqui = aqui
        self.floresta_chuva = None
    def vai(self):
        from chuva.main import FlorestaChuva
        self.floresta_chuva = FlorestaChuva(self.aqui)
        self.floresta_chuva.esquerda = self.aqui
        self.floresta_chuva.vai()


class Cobra:
    def __init__(self, floresta_inicio):
        self.floresta_inicio = floresta_inicio
        self.cobra = Elemento(COBRA, style=dict(left="800px", width="150px"))
        self.cobra.entra(floresta_inicio)
        self.cobra.vai()
        
    def vai(self):
        self.floresta_inicio.vai()
        
class EntradaCaverna:
    def __init__(self, caverna=None):
        legenda = "A entrada da caverna escura"
        self.caverna = caverna
        atores = dict(lanterna=self.ilumina_caverna)
        self.entrada = Elemento(ENTRADA, tit=legenda, x=340, y=80, w=600, h=600, style={"opacity": 0.009},
            drop=atores, cena=caverna)
    def ilumina_caverna(self, evento, objeto):
        self.entrada.elt.style.opacity=0.05
        Texto(self.caverna, "Você ilumina a caverna, mas não encontra a mãe do macaquinho").vai()
    def vai(self, evento, objeto):
        Texto(self.caverna, "A caverna é muito escura, você precisa iluminar a caverna").vai()
        
class Caverna:
    def __init__(self, esquerda=None):
        # floresta_faca = FlorestaFaca() -XX- ERRO!
        self.floresta_inicio = None
        floresta_chuva = CenaProxy(self.floresta_inicio)
        esquerda = esquerda or floresta_chuva
        self.floresta_inicio = Cena(CAVERNA, esquerda=esquerda, direita=floresta_chuva)
        # INVENTARIO.bota("lanterna","https://i.imgur.com/Z4DAh02.png",drag=True)
        # INVENTARIO.bota("capa de chuva",CAPA_DE_CHUVA)
        self.entrada = EntradaCaverna(self.floresta_inicio)
        self.cavernatexto = Texto(self.floresta_inicio, TEXTO_CAVERNA)
        self.floresta_inicio.meio=self.cavernatexto
        # banana = Banana(self.floresta_inicio)
        # rede = Rede(self.floresta_inicio)
        
        
    def vai(self):
        Texto(self.floresta_inicio, "Aqui tem uma caverna muito escura, será que a mãe do macaquinho está aqui?").vai()
        self.floresta_inicio.vai()
                
if __name__ == "__main__":
    INVENTARIO.inicia()
    a_floresta = Caverna()
    a_floresta.vai()