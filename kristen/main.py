# vera.kristen.main.py
from _spy.vitollino.main import Cena
from random import shuffle

IMAGENS = ["TEMPLO", "TESOURO", "FOGO", "ARTEFATO1", "COBRA", "DESABAMENTO", "MUMIA", "ARANHA"]
DI = DICIONARIO_DE_IMAGENS = {}
DI["TEMPLO"] = "https://i.imgur.com/LXptu0U.jpg"
DI["TESOURO"] = "https://i.imgur.com/Nq1hCeU.jpg"
DI["FOGO"] = "https://i.imgur.com/KRK66bR.jpg"
DI["ARTEFATO1"] = "https://i.imgur.com/1QHNdyI.jpg"
DI["COBRA"] = "https://i.imgur.com/MydpgBT.jpg"
DI["DESABAMENTO"] = "https://i.imgur.com/jnxWklS.jpg"
DI["MUMIA"] = "https://i.imgur.com/HPp1k5T.jpg" 
DI["ARANHA"] = "https://i.imgur.com/w90m1jf.jpg"

class Inca:
    def inicia(self):
        templo = Cena(DI["TEMPLO"])
        tesouro = Cena(DI["TESOURO"])
        fogo = Cena(DI["FOGO"])
        artefato1 = Cena(DI["ARTEFATO1"])
        cobra = Cena(DI["COBRA"])
        desabamento = Cena(DI["DESABAMENTO"])
        mumia = Cena(DI["MUMIA"])
        aranha = Cena(DI["ARANHA"])

inca = Inca()

if __name__ == "__main__":
    inca.inicia()

class Cartas:
    def baralho(self):
        return []
    pass
    
class Jogo:
    def __init__(self):
        self.baralho = Cartas().baralho()
        self.templo = Cena(DI["TEMPLO"])
    def inicia(self):
        self.templo.vai()
    
def decisao (anterior,carta):
    resposta = input ("Você descobriu uma câmara do templo. Você entra nela ou sai?")
    if resposta == "entro": 
        carta.vai() 
    elif resposta == "saio":
        anterior.vai()

baralho = (DI["FOGO"](), DI["TESOURO"](), DI["ARANHA"], DI["MUMIA"], DI["ARTEFATO1"], DI["DESABAMENTO"], DI["COBRA"])
shuffle(baralho)
umacarta = baralho[0]
umacarta.vai()

#cartas = [TESOURO(), ARTEFATO1(), FOGO(), MUMIA(), DESABAMENTO(), ARANHA(), COBRA()]
#baralho = cartas[:] # Copy cartas
#shuffle(baralho) # Shuffle baralho
#for elemento in cartas:
 #   elemento.vai()



