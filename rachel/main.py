# vera.rachel.main.py
"http://supygirls.pythonanywhere.com"
from _spy.vitollino.main import Cena, Elemento
# from amanda.main import FlorestaFaca
FLORESTA = "https://i.imgur.com/VHaolvA.jpg"
BANANA = "https://i.imgur.com/HnIHJd7.png"

class CenaProxy:
    def __init__(self, aqui=None):
        self.aqui = aqui
        self.floresta_faca = None
    def vai(self):
        from amanda.main import FlorestaFaca
        self.floresta_faca = FlorestaFaca()
        self.floresta_faca.esquerda = self.aqui
        self.floresta_faca.vai()
        
class Florestabanana:
    def __init__(self):
    # floresta_faca = FlorestaFaca() -XX- ERRO!
    self.floresta_inicio = None
        floresta_faca = CenaProxy(self.floresta_inicio)
        self.floresta_inicio = Cena(FLORESTA, direita=floresta_faca)
        banana = Elemento(BANANA, style=dict(left="230px", width="50px"))
        banana.entra(self.floresta_inicio)
        
    def vai(self):
        self.floresta_inicio.vai()
        
if __name__ == "__main__":
    a_floresta = FlorestaBanana()
    a_floresta.vai()