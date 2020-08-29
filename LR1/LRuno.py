from Gramatica.Produccion import Produccion
from LR1.Cerradura import Cerradura


class LRcero:

    def __init__(self, gramatica):
        self.grammar = gramatica
        self.aumentarGramatica()
        self.cerraduras = []
        self.contador = 0
        #self.analizar(Cerradura("I" + str(self.contador), self.verificarPosPunto([self.aumentada[0]]), [], []))

    def aumentarGramatica(self):
        nueva = Produccion(self.grammar.getProduccionInicial().getNoTerminal() + "'",
                           "°" + self.grammar.getProduccionInicial().getNoTerminal())
        self.aumentada = []
        self.aumentada.append(nueva)
        for pd in self.grammar.getProducciones():
            pd.agregarPunto()
            self.aumentada.append(pd)

    def calcularPrimeros(self):
        self.primeros = {}
        noTerminales = self.grammar.getNoTerminales()
        producciones = self.grammar.getProducciones()
        for nt in noTerminales:
            primeros = []
            for p in producciones:
                if nt == producciones.getNoTerminal():
                    primero = p.getProduccion()[0]
                    if primero == self.grammar.getTerminales():
                        primeros.append(primero)
                    else:
                        self.primerosNoterminal(primero)
            self.primeros.update({nt: primeros})

    def primerosNoterminal(self,nt, primeros = []):
        producciones = self.grammar.getProducciones()
        for p in producciones:
            if nt == producciones.getNoTerminal():
                primero = p.getProduccion()[0]
                if primero == self.grammar.getTerminales():
                    primeros.append(primero)
                else:
                    self.primerosNoterminal(primero,primeros)
        return primeros
