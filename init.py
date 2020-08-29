from Gramatica.Produccion import Produccion
from Gramatica.Gramatica import Gramatica
from LR0.LRcero import LRcero

if __name__ == '__main__':

    producciones = [Produccion("E","E+ni"),Produccion("E","ni")]
    G = Gramatica(["E"],["+","ni"],Produccion("E","E+ni"),producciones)

    #producciones = [Produccion("S", "L=R"), Produccion("S", "R"),Produccion("L", "*R"),Produccion("L", "id"),Produccion("R", "L")]
    #G = Gramatica(["S","L","R"], ["*", "id","="], Produccion("S", "L=R"), producciones)

    lr = LRcero(G)
    """
    caa = "casas"

    print(caa.split("c"))
    """
    cerraduras = lr.cerraduras
    print(len(cerraduras))
    for c in cerraduras:
        print(c.estado)
        print("Accion"+str(c.getActions()))
        print("IR_A" + str(c.getIra()))
        print("Reduccion "+str(c.getReduccion()))
        for i in c.prod:
            print(i.getNoTerminal()+" -> "+i.getProduccion())
        print("----------------------------------------------")
