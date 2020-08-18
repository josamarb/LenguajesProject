from Gramatica.Produccion import Produccion
from LR.Cerradura import Cerradura

class LRcero:

    def __init__(self,gramatica):
        self.grammar = gramatica
        self.aumentarGramatica()
        self.cerraduras=[]
        self.contador = 0
        self.analizar(Cerradura("I"+str(self.contador),self.verificarPosPunto([self.aumentada[0]]),[],[]))

    def aumentarGramatica(self):
        nueva = Produccion(self.grammar.getProduccionInicial().getNoTerminal()+"'","°"+self.grammar.getProduccionInicial().getNoTerminal())
        self.aumentada = []
        self.aumentada.append(nueva)
        for pd in self.grammar.getProducciones():
            pd.agregarPunto()
            self.aumentada.append(pd)

    def getGramaticaAumentada(self):
        return self.aumentada

    def analizar(self,cerradura):
        for g in cerradura.getProducciones():
            p = g.getProduccion()
            pos = p.index("°")
            if pos + 1 < len(p):
                transition= self.getTransition(p,pos)
                tempProducciones = self.moverPunto(transition,cerradura.getProducciones())
                producciones = self.verificarPosPunto(tempProducciones)
                nuevaCerradura = self.cerraduraExist(producciones)
                if not nuevaCerradura:
                    self.contador = self.contador + 1
                    nuevaCerradura = Cerradura("I"+str(self.contador),producciones,[],[])
                if self.isTerminal(transition):
                    cerradura.agregarAccion((transition,nuevaCerradura.getNombreEstado()))
                else:
                    cerradura.agregarIra((transition,nuevaCerradura.getNombreEstado()))
                self.analizar(nuevaCerradura)
            else:
                cerradura.setReduccion("R" + str(self.getPosicionProduccion(p)))
        if not cerradura in self.cerraduras:
            self.cerraduras.append(cerradura)



    def isTerminal(self,char):
        if char in self.grammar.getNoTerminales():
            return False
        return True


    def moverPunto(self,transition,producciones):
        estado = []
        for gram in producciones:
            p = gram.getProduccion()
            pos = p.index("°")
            if pos + 1 != len(p):
                trans=self.getTransition(p,pos)
                if trans == transition:
                    nuevaProduccion = self.ponerPunto(p,pos+len(trans))
                    nueva = Produccion(gram.getNoTerminal(),nuevaProduccion)
                    estado.append(nueva)
        return estado

    def verificarPosPunto(self,producciones):
        nuevasProduccion =[]
        nuevasProduccion.extend(producciones)
        for prod in producciones:
            p = prod.getProduccion()
            pos = p.index("°")
            if pos+1 != len(p):
                caracter=p[pos+1]
                if caracter in self.grammar.getNoTerminales():
                    for gram in self.aumentada:
                        if gram.getNoTerminal() == caracter:
                            nuevasProduccion.append(gram)
        return nuevasProduccion


    def ponerPunto(self,produccion,position):

        split = produccion.split("°")
        prod = split[0]+split[1]
        conPunto = ""
        for p in range(len(prod)):
            conPunto = conPunto + prod[p]
            if p==position-1:
                conPunto = conPunto+"°"
        return conPunto

    def cerraduraExist(self,producciones):
        for c in self.cerraduras:
            if self.compararProducciones(c.getProducciones(),producciones):
                return c
        return None

    def compararProducciones(self,produccion1, produccion2):
        if len(produccion1) == len(produccion2):
            contador = 0
            for i in range(len(produccion1)):
                if produccion1[i].getNoTerminal() == produccion2[i].getNoTerminal() and produccion1[i].getProduccion() == produccion2[i].getProduccion():
                    contador=contador+1
            if contador==len(produccion2):
                return True
        return False

    def getTransition(self,produccion,posicion):
        i = 1
        trans = produccion[posicion + i]
        if trans in self.grammar.getNoTerminales():
            return trans
        else:
            isNoTerminal = True
            while isNoTerminal:
                if trans in self.grammar.getTerminales():
                    isNoTerminal=False
                else:
                    i=i+1
                    trans= trans+produccion[posicion+i]
        return trans
    def getPosicionProduccion(self, produccion):
        aumentada = self.getGramaticaAumentada()
        for i in range(len(aumentada)):
            if aumentada[i].getProduccion().split("°")[1] == produccion.split("°")[0]:
                return i
        return -1