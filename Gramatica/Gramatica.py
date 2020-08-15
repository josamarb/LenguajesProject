from Gramatica.Produccion import Produccion

class Gramatica:

    def __init__(self,noTerminales,terminales,produdccionInicial,producciones):
        self.nt = noTerminales
        self.t = terminales
        self.s = produdccionInicial
        self.p = producciones

    def getNoTerminales(self):
        return self.nt

    def getTerminales(self):
        return self.t

    def getProduccionInicial(self):
        return self.s

    def getProducciones(self):
        return self.p