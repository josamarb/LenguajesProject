class Cerradura:

    def __init__(self,estado,producciones,terminales ,ira):
        self.estado =estado
        self.prod = producciones
        self.terminales = terminales
        self.ira = ira
        self.reduccion = ''

    def getNombreEstado(self):
        return self.estado

    def getProducciones(self):
        return self.prod

    def getTerminales(self):
        return self.terminales

    def getIra(self):
        return self.ira

    def agregarAccion(self,action):
        if not action in self.terminales:
            self.terminales.append(action)

    def agregarIra(self,ira):
        if not ira in self.ira:
            self.ira.append(ira)

    def setReduccion(self,R):
        self.reduccion = R

    def getReduccion(self):
        return self.reduccion