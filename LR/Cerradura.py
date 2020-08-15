class Cerradura:

    def __init__(self,estado,producciones,accion ,ira):
        self.estado =estado
        self.prod = producciones
        self.accion = accion
        self.ira = ira
        self.reduccion = ''

    def getNombreEstado(self):
        return self.estado

    def getProducciones(self):
        return self.prod

    def getActions(self):
        return self.accion

    def getIra(self):
        return self.ira

    def agregarAccion(self,action):
        if not action in self.accion:
            self.accion.append(action)

    def agregarIra(self,ira):
        if not ira in self.ira:
            self.ira.append(ira)

    def setReduccion(self,R):
        self.reduccion = R