
class Produccion:

    def __init__(self, noTerminal, produccion):
        self.noterminal = noTerminal
        self.produccion = produccion

    def getNoTerminal(self):
        return self.noterminal

    def getProduccion(self):
        return self.produccion

    def agregarPunto(self,produccion):
        return "°"+produccion
