# vera.trilhacaverna.main.py
from _spy.vitollino.main import Cena, STYLE
STYLE["width"], STYLE["height"] = 1200, "650px"
from elemento.main import Elemento
TRILHACAVERNA = "https://i.imgur.com/bNEzuBs.jpg"
ARANHA = "https://i.imgur.com/xXPifks.png"
COBRA = "https://i.imgur.com/EoIRfsD.png"
trilhacaverna = Cena(TRILHACAVERNA)
trilhacaverna.vai()
aranha = Elemento (ARANHA, cena = trilhacaverna, x= 800, y= 200, w= 200, h= 200)
cobra = Elemento (COBRA, cena = trilhacaverna, x= 300, y= 450, w= 400, h= 200)


