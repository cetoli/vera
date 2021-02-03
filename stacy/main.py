# vera.sarah.main.py
from _spy.vitollino.main import Cena, Texto, INVENTARIO, STYLE
from elemento.main import Elemento
# from morgan.main import FlorestaLeao
STYLE["width"], STYLE["height"] = 1400, "650px"

FOGUETE = "https://i.imgur.com/Q33m8SY.png" 
JANELA = "https://i.imgur.com/hITHdyc.png"
ESTACAO = "https://i.imgur.com/ybteKID.png"
TERRA = "https://i.imgur.com/rJJHQJj.png"
UNIVERSO = "https://i.imgur.com/tjT0IqM.jpg"
DOCA = "https://i.imgur.com/NMLjvWU.png"
PESSOA = "https://i.imgur.com/Mt5juow.png"
ANIMAL = "https://i.imgur.com/falELaz.png"
OBJETO = "https://i.imgur.com/iXQYTtn.png"
IMGUR = "https://i.imgur.com/{}.png"
PESSOAS = [IMGUR.format(icone) for icone in "H0sLGRO.png rJXklVA.png WjXPkDj.png 31bHmRB.png kSEbjOG.png "]
IMGUR = "https://i.imgur.com/{}"
MENUDEANIMAIS = [IMGUR.format(icone) for icone in ["vsFMB8U.jpg","6LKzi5g.jpg","eE9SXr2.png","UvMSgka.png"]]
MENUDEOBJETOS = [IMGUR.format(icone) for icone in ["mwzJSyB.jpg","AZCRF7a.png","X2nJzqY.png","P3FmARs.png","3p3erLe.png"]]
MENUDEPESSOAS = [IMGUR.format(icone) for icone in ["3WAuJEJ.jpg","b9qGgwO.jpg","wdFwoKb.png","UJeIu1G.png",
"MItp8Gn.png","msjPkhL.png","8THmFvb.png","TjouWWp.jpg","6tM3VXW.jpg","QnhIR2A.jpg","fQcHTky.jpg","yC6LfXF.jpg",
"yC6LfXF.jpg","Mlu928W.jpg","xw2IiTT.jpg","KY070ZY.png","AHoLboo.png"]]
class CenaProxy:
    def __init__(self, aqui=None):
        self.aqui = aqui
        self.floresta_leao = None
    def vai(self):
        from morgan.main import FlorestaLeao
        self.floresta_leao = FlorestaLeao()
        self.floresta_leao.esquerda = self.aqui
        self.floresta_leao.vai()

"""
class Estacao:
    def __init__(self, universo):
        self.floresta_inicio = floresta_inicio
        self.fala = Texto(self.floresta_inicio, TEXTO_FACA)
        self.falou = Texto(self.floresta_inicio, FACA_FOI)
        self.usar = Texto(self.floresta_inicio, FACA_USA)
        # self.faca = Elemento(FACA, style=dict(left="200px", width="80px"), vai=self.pega)
        self.faca = Elemento(FACA, tit="faca", x=600, y=500, w=80, vai=self.pega)
        self.longe = Cena()
        self.na_mao = False
        self.faca.entra(self.floresta_inicio)
    
    def pega(self, _):
        self.fala.vai()
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
"""

class Terra:
    def __init__(self, universo):
        self.universo = universo
        """
        self.fala = Texto(self.universo, TEXTO_FACA)
        self.falou = Texto(self.universo, FACA_FOI)
        self.usar = Texto(self.universo, FACA_USA)
        """
        self.terra = Elemento(TERRA, x=800, y=180, w=450, h=400, vai=self.pega)
        self.longe = Cena()
        self.na_mao = False
        self.terra.entra(self.universo)
    
    def pega(self, _):
        self.fala.vai()
        self.faca.vai = self.guarda
        
class Foguete:
    def __init__(self, universo, left=200, top=50):
        self.universo = universo
        self.foguete = Elemento(FOGUETE, x=left, y=top, w=150, h=150, vai=self.pega)
        self.longe = Cena()
        self.na_mao = False
        self.foguete.entra(self.universo)
    
    def pega(self, _):
        self.foguete.vai()
        self.foguete.vai = self.guarda
        
class Doca:
    def __init__(self, universo, left="300px", top="300px"):
        self.universo = universo
        self.doca = Elemento(DOCA, x=left, y=top, w=200, h=300, vai=self.pega, style={"transform": "rotate(300deg)"})
        self.longe = Cena()
        self.na_mao = False
        self.doca.entra(self.universo)
    
    def pega(self, _):
        self.doca.vai()
        self.doca.vai = self.guarda


class Estacao:
    def __init__(self, universo, menu, left="300px", top="300px", icone=PESSOA, ITENS=[]):
        def add(valor, num):
            return "{}px".format(int(valor[:-2]) + num)
        self.universo = universo
        """
        self.fala = Texto(self.universo, TEXTO_FACA)
        self.falou = Texto(self.universo, FACA_FOI)
        self.usar = Texto(self.universo, FACA_USA)
        """
        self.estacao = Elemento(ESTACAO, x=left, y=top, w=300, h=240, vai=self.pega)
        self.icone = Elemento(icone, style=dict(left=add(left,55),
            top=add(top,85), width="400px", height="40px"), vai=self.pega)
        self.janela = Elemento(JANELA, style=dict(left=add(left,50), top=add(top,80), width="500px", height="50px"), vai=self.pega)
        self.longe = Cena()
        self.na_mao = False
        self.estacao.entra(self.universo)
        self.janela.entra(self.universo)
        self.icone.entra(self.universo)
        self.menu =menu
    
    def pega(self, _):
        #self.fala.vai()
        #self.faca.vai = self.guarda
        #Menudeanimais(self.universo)
        self.menu.abre()
"""    
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
"""    
    
    
class Menudeanimais:
    def __init__(self, universo, left=200, top=50):
        self.universo = u = universo
        self.longe = Cena()
        self.na_mao = False
        self.left, self.top = left, top
            
    def abre(self):        
        left, top, u = self.left, self.top, self.universo
        self.menudeanimais = Elemento(MENUDEANIMAIS[0], x=left -170, y=top, w=60, h=60, vai=self.pega, cena=u)
        self.menudeanimais = Elemento(MENUDEANIMAIS[1], x=left +40, y=top +1, w=60, h=60, vai=self.pega, cena=u)
        self.menudeanimais = Elemento(MENUDEANIMAIS[2], x=left-30, y=top +1, w=60, h=60, vai=self.pega, cena=u)
        self.menudeanimais = Elemento(MENUDEANIMAIS[3], x=left -100, y=top, w=60, h=60, vai=self.pega, cena=u)
        #self.menudeanimais.entra(self.universo)
    
    def pega(self, _):
        self.menudeanimais.vai()
        #self.menudeaminais.vai = self.guarda
        
        
        
class Menudeobjetos:
    def __init__(self, universo, left=200, top=50):
        self.universo = universo
        self.left, self.top = left, top
            
    def abre(self):        
        left, top, u = self.left, self.top, self.universo
        self.menudeobjetos = Elemento(MENUDEOBJETOS[0], x=left -170, y=top +50, w=60, h=60, vai=self.pega,cena=self.universo)
        self.menudeobjetos = Elemento(MENUDEOBJETOS[1], x=left +30, y=top +50, w=60, h=60, vai=self.pega,cena=self.universo)
        self.menudeobjetos = Elemento(MENUDEOBJETOS[2], x=left -40, y=top +50, w=60, h=60, vai=self.pega,cena=self.universo)
        self.menudeobjetos = Elemento(MENUDEOBJETOS[3], x=left -260, y=top +50, w=80, h=80, vai=self.pega,cena=self.universo)
        self.menudeobjetos = Elemento(MENUDEOBJETOS[4], x=left -110, y=top +50, w=60, h=60, vai=self.pega,cena=self.universo)
        self.longe = Cena()
        self.na_mao = False
        # self.menudeobjetos.entra(self.universo)
    
    def pega(self, _):
        self.menudeobjetos.vai()
        #self.menudeobjetos.vai = self.guarda
        
class Menudepessoas:
    def __init__(self, universo, left=200, top=50):
        self.universo = universo
        self.left, self.top = left, top
            
    def abre(self):        
        left, top, u = self.left, self.top, self.universo
        self.menudepessoas = Elemento(MENUDEPESSOAS[0], x=left -170, y=top +50, w=60, h=60, vai=self.pega,cena=self.universo)
        self.menudepessoas = Elemento(MENUDEPESSOAS[1], x=left +30, y=top +50, w=60, h=60, vai=self.pega,cena=self.universo)
        self.menudepessoas = Elemento(MENUDEPESSOAS[2], x=left -40, y=top +50, w=60, h=60, vai=self.pega,cena=self.universo)
        self.menudepessoas = Elemento(MENUDEPESSOAS[3], x=left -260, y=top +50, w=80, h=80, vai=self.pega,cena=self.universo)
        self.menudepessoas = Elemento(MENUDEPESSOAS[4], x=left -110, y=top +50, w=60, h=60, vai=self.pega,cena=self.universo)
        self.longe = Cena()
        self.na_mao = False
        # self.menudeobjetos.entra(self.universo)
    
    def pega(self, _):
        self.menudepessoas.vai()
        #self.menudeobjetos.vai = self.guarda
        
class Universo:
    def __init__(self):
        # floresta_leao = FlorestaLeao() -XX- ERRO!
        self.universo = None
        deserto = CenaProxy(self.universo)
        self.universo = Cena(UNIVERSO)
        terra = Terra(self.universo)
        menu = Menudeanimais(self.universo)
        menuo = Menudeobjetos(self.universo, left=380, top=410)
        menup = Menudepessoas(self.universo, left=280, top=150)
        estacao = Estacao(self.universo, menup, left="280px", top="150px", icone=PESSOA)
        estacao2 = Estacao(self.universo, menu, left="30px", top="50px", icone=ANIMAL)
        estacao3 = Estacao(self.universo, menuo, left="380px", top="410px", icone=OBJETO)
        foguete = Foguete(self.universo, left=20, top=500)
        doca = Doca(self.universo, left="650px", top="250px")
        
              
    def vai(self):
        self.universo.vai()

        
if __name__ == "__main__":
    INVENTARIO.inicia()
    o_universo = Universo()
    o_universo.vai()
